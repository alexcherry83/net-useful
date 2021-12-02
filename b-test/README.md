To start a p rogram you need to get a TCP file from certain interface first, please use command 
tcpdump -i en0 -e > test5.dump, where en0 is the interface to track

then start a script tcpdump_btest.tcp test5.dump, 
it will show the bandwidth speed and also the bandwidth/speed per each session
