#!/usr/bin/env python3

def c_class(ipv4):
	
	mask=ipv4[0].split('/')
	ip=str(mask[0]).split('.')
	ip_bin=[bin(int(ip[0]))[2:].zfill(8),bin(int(ip[1]))[2:].zfill(8),bin(int(ip[2]))[2:].zfill(8),bin(int(ip[3]))[2:].zfill(8)]

#After first steps we got list ip with [string] with decimal IP and ip_bin list [strings] with binary data


# prepare a list with 32 elements = 32 bits with values 0

	x=[]
	for i in range(32):
	    x.append('0')

# now put 1s to all elements of list until mask bits exists /24 = 24 bits with 1s

	i=0
	while i<int(mask[1]):
		x[i]='1'
		i=i+1


#we need to split 32 elements into 4 parts with 8 bits
	x1,x2,x3,x4=[],[],[],[]

	i=0
	while i<8:
		x1.append(x[i])
		i+=1

	while i<16:
		x2.append(x[i])
		i+=1
	
	while i<24:
		x3.append(x[i])
		i+=1
	
	while i<32:
		x4.append(x[i])
		i+=1

	mask_bin=[''.join(x1),''.join(x2),''.join(x3),''.join(x4)]
	mask_dec=[int(mask_bin[0],2),int(mask_bin[1],2),int(mask_bin[2],2),int(mask_bin[3],2)]

#Now we have IP in dec, IP in bin, Mask in dec and Mask in bin.

#Calculate network address

	net_addr=[(int(ip[0]) & int(mask_dec[0])),(int(ip[1]) & int(mask_dec[1])),(int(ip[2]) & int(mask_dec[2])),(int(ip[3]) & int(mask_dec[3]))]


#Split network to /24 networks and create a list with all /24 networks

#how many /24 are in our network ?

	wildcard_mask=[(256-mask_dec[0]), (256-mask_dec[1]), (256-mask_dec[2]), (256-mask_dec[3])]

	net_amount=(wildcard_mask[0]*wildcard_mask[1]*wildcard_mask[2])


#let's create a list 

	net_list=[]
	for nt in range(4):
		net_list.append([])

	factor = int(net_amount/256)

	if factor<=1:
		for st in range(net_amount):
			net_list[0].append(net_addr[0])
			net_list[1].append(net_addr[1]) 
			net_list[2].append(net_addr[2]+st)
			net_list[3].append(0)


	if factor>1 and factor<256:
		for xt in range(factor):
			for st in range(256):
				net_list[0].append(net_addr[0])
				net_list[1].append(net_addr[1]+xt) 
				net_list[2].append(net_addr[2]+st)
				net_list[3].append(0)


	if factor>255 and factor<65536:
		for yt in range(int(factor/256)):
			for xt in range(factor):
				for st in range(256):
					net_list[0].append(net_addr[0]+yt)
					net_list[1].append(net_addr[1]+xt) 
					net_list[2].append(net_addr[2]+st)
					net_list[3].append(0)

	return net_list