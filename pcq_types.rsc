# apr/05/2018 14:20:47 by RouterOS 6.41.3
# software id = 
#
#
#
/queue type
add kind=pcq name=SpLPCQGroup_1-DOWN pcq-classifier=dst-address pcq-rate=\
    2048k
add kind=pcq name=SpLPCQGroup_1-UP pcq-classifier=src-address pcq-rate=512k
add kind=pcq name=SpLPCQGroup_2-DOWN pcq-classifier=dst-address pcq-rate=5M
add kind=pcq name=SpLPCQGroup_2-UP pcq-classifier=src-address pcq-rate=1024k
add kind=pcq name=SpLPCQGroup_3-DOWN pcq-classifier=dst-address pcq-rate=\
    10240k
add kind=pcq name=SpLPCQGroup_3-UP pcq-classifier=src-address pcq-rate=2048k
add kind=pcq name=SpLPCQGroup_4-DOWN pcq-classifier=dst-address pcq-rate=\
    5192k
add kind=pcq name=SpLPCQGroup_4-UP pcq-classifier=src-address pcq-rate=2048k
add kind=pcq name=SpLPCQGroup_5-DOWN pcq-classifier=dst-address pcq-rate=\
    10240k
add kind=pcq name=SpLPCQGroup_5-UP pcq-classifier=src-address pcq-rate=2048k
add kind=pcq name=SpLPCQGroup_6-DOWN pcq-classifier=dst-address pcq-rate=\
    2048k
add kind=pcq name=SpLPCQGroup_6-UP pcq-classifier=src-address pcq-rate=2048k
