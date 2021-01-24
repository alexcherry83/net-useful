#!/usr/bin/env python
from sys import argv

#my_ip = argv[1]

def ip_check(ip_address):
    ip = ip_address.split(".")

    if (ip.__len__()) != 4:
        print ("You haven't entered the valid IP address with a '.' notation")
        ip_address = ip_check(input("Please enter IP address : "))
    else  :
        try:
            for i in ip:
                if (int(i)<0) or (int(i)>255):
                    ip_address = ip_check(input("Please enter valid IP address : "))
                    break
        except:
            print("Sorry, you haven't entered the valid IP address : ")
            ip_address = ip_check(input("Please enter IP address : "))
    return(ip_address)

def find_net(ip_address) :
    ip = ip_address.split(".")
    net = [ip[0],ip[1],ip[2],"0"]
    my_net = ".".join(net)
    return(my_net)

#ip_check(my_ip)