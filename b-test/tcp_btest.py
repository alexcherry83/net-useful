import datetime
import json
from tabulate import tabulate
from operator import itemgetter

class tcp_bandwidth_test:
    def __init__(self, data_list):
        self.data_list = data_list

    def get_tcp_stats(self):
        # Creating a list of unique SRC-DST combinations
        unique_combinations = []
        for i in self.data_list :
            unique_combinations.append(i['session'])
        u_combinations = set(unique_combinations)

        #Creating unique combination list where SRC is in first element and DST in the second
        session_list = []
        for line in u_combinations:
            data = line.split('<->')
            data_dict = {data[0]:data[1]}
            session_list.append(data_dict)

        #Now we need to select only unique sessions, select only one SRC-DST and DST-SRC combination
        final_sessions = []

        id=0
        for line in session_list:
            for key in line:
                SRC = key
                DST = line[key]
                for line1 in session_list:
                    for key1 in line1:
                        SRC1 = key1
                        DST1 = line1[key1]
                        if DST1 == SRC and SRC1==DST:
                            final_sessions.append(line1)
                            session_list[id][key]="USED_IPS"
            id = id + 1

        #Let's sort all stats according to sessions
        sorted_stats=[]
        for session in final_sessions:
            for key in session:
                SRC = key
                DST = session[key]
                for packet in self.data_list:
                    if packet['src'] == SRC and packet['dst'] == DST:
                        data = {SRC+" <-> "+DST : packet}
                        sorted_stats.append(data)
                    if packet['dst'] == SRC and packet['src'] == DST:
                        data = {SRC+" <-> "+DST : packet}
                        sorted_stats.append(data)

        #print(json.dumps(sorted_stats, indent=4))
        #print(len(sorted_stats))

        #Next step is to show each sessions:
        #0. Session name
        #1. Start time
        #2. End time
        #3. Amount of packets
        #4. Data transferred UP + Down
        #5. Speed UP+DOWN of each session

        final_statistics=[]
        for session in final_sessions:
            for key in session:
                name = key+" <-> "+session[key]
                time_counter = 0
                packet_counter = 0
                data_counter = 0

                for stat_line in sorted_stats:
                    for stat_key in stat_line:
                        if name==stat_key:
                            packet_counter=packet_counter+1
                            data_counter=data_counter+stat_line[stat_key]["frame_size"]
                            if time_counter==0:
                                start_time = stat_line[stat_key]["timestamp"]
                            time_counter=time_counter+1
                            end_time = stat_line[stat_key]["timestamp"]
                            src_ip = stat_line[stat_key]["src_ip"]
                            dst_ip = stat_line[stat_key]["dst_ip"]

            time_delta = datetime.datetime.strptime(end_time, "%H:%M:%S.%f") - datetime.datetime.strptime(start_time,"%H:%M:%S.%f")
            speed_mbps = round(data_counter*8/1024/1024/float(time_delta.total_seconds()),3)
            data = {'name': name, 'start_time': start_time, 'session_duration' : float(time_delta.total_seconds()), 'amount_packets' : packet_counter, 'data_transferred' : round(data_counter/1024/1024,6), 'speed' : str(speed_mbps)+" Mbps"}
            final_statistics.append(data)


        final_statistics.sort(key=itemgetter('amount_packets'),reverse=True)
        print(tabulate(final_statistics, headers='keys', tablefmt="grid"))

        dump_start_time = self.data_list[0]["timestamp"]
        dump_end_time = self.data_list[-1]["timestamp"]
        dump_time_delta = datetime.datetime.strptime(dump_end_time,"%H:%M:%S.%f") - datetime.datetime.strptime(dump_start_time,"%H:%M:%S.%f")

        print("Total duration of dump : " + str(float(dump_time_delta.total_seconds())) + " seconds")

        print("Amount of TCP sessions " + str(len(final_statistics)))

        packets=0
        for paq in final_statistics:
            packets = packets + paq['amount_packets']

        print("Amount of packets " + str(packets))

        all_data=0
        for line in final_statistics:
            all_data = all_data + line['data_transferred']

        print("Data transferred : " + str(all_data) + " MB")
        av_speed = round(all_data*8/float(dump_time_delta.total_seconds()),3)

        print("Average speed is " + str(av_speed) + " Mbps")