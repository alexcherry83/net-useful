# apr/05/2018 14:16:57 by RouterOS 6.41.3
# software id = 
#
#
#
/queue simple
add burst-time=10s/10s comment=10001 limit-at=51k/205k max-limit=512k/2048k \
    name=SpLSQ_1-1 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.2/32
add burst-time=10s/10s comment=20002 limit-at=51k/205k max-limit=512k/2048k \
    name=SpLSQ_2-2 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.3/32
add burst-time=10s/10s comment=30003 limit-at=51k/205k max-limit=512k/2048k \
    name=SpLSQ_3-3 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.4/32
add burst-time=10s/10s comment=10004 limit-at=51k/205k max-limit=512k/2048k \
    name=SpLSQ_4-4 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.5/32
add burst-time=10s/10s comment=20005 limit-at=51k/205k max-limit=512k/2048k \
    name=SpLSQ_5-5 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.6/32
add burst-time=10s/10s comment=30006 limit-at=102k/500k max-limit=1024k/5M \
    name=SpLSQ_6-6 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.7/32
add burst-time=10s/10s comment=10007 limit-at=102k/500k max-limit=1024k/5M \
    name=SpLSQ_7-7 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.8/32
add burst-time=10s/10s comment=20008 limit-at=102k/500k max-limit=1024k/5M \
    name=SpLSQ_8-8 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.9/32
add burst-time=10s/10s comment=30009 limit-at=102k/500k max-limit=1024k/5M \
    name=SpLSQ_9-9 priority=5/5 queue=pcq-download-default/pcq-upload-default \
    target=192.168.100.10/32
add burst-time=10s/10s comment=40010 limit-at=102k/500k max-limit=1024k/5M \
    name=SpLSQ_10-10 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.11/32
add burst-time=10s/10s comment=40011 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSQ_11-11 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.12/32
add burst-time=10s/10s comment=50012 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSQ_12-12 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.13/32
add burst-time=10s/10s comment=50013 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSQ_13-13 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.14/32
add burst-time=10s/10s comment=50014 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSQ_14-14 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.17/32
add burst-time=10s/10s comment=10015 limit-at=205k/205k max-limit=2048k/2048k \
    name=SpLSQ_15-15 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.15/32
add burst-time=10s/10s comment=10016 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSQ_16-16 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.16/32
add burst-time=10s/10s comment=40017 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSQ_17-17 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.18/32
add burst-time=10s/10s comment=30018 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSQ_18-18 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.19/32
add burst-time=10s/10s comment=20019 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSQ_19-19 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.24/32
