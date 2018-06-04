# apr/16/2018 10:20:45 by RouterOS 6.41.3
# software id = 
#
#
#
/queue simple
add burst-time=10s/10s comment="Tariff Main-Home Internet 2 Mbps" limit-at=\
    51k/205k max-limit=512k/2048k name=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target="192.168.100.2/32,192.168.1\
    00.3/32,192.168.100.4/32,192.168.100.5/32,192.168.100.6/32"
add burst-time=10s/10s comment="Tariff Main-Home Internet 5 Mbps" limit-at=\
    102k/500k max-limit=1024k/5M name=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target="192.168.100.7/32,192.168.1\
    00.8/32,192.168.100.9/32,192.168.100.10/32,192.168.100.11/32"
add burst-time=10s/10s comment="Tariff Main-Home Internet 10 Mbps" limit-at=\
    205k/1024k max-limit=2048k/10240k name=SpLSTG_0-3 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.12/32
add burst-time=10s/10s comment="Tariff Main-Business 5 Mbps" limit-at=\
    615k/1557k max-limit=6144k/15576k name=SpLSTG_0-4 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=\
    192.168.100.13/32,192.168.100.14/32,192.168.100.24/32
add burst-time=10s/10s comment="Tariff Main-Business 10 Mbps" limit-at=\
    820k/4096k max-limit=8192k/40960k name=SpLSTG_0-5 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=\
    192.168.100.17/32,192.168.100.16/32,192.168.100.18/32,192.168.100.19/32
add burst-time=10s/10s comment="Tariff Main-Capped 2 Mbps, 3GB included" \
    limit-at=205k/205k max-limit=2048k/2048k name=SpLSTG_0-6 priority=5/5 \
    queue=pcq-download-default/pcq-upload-default target=192.168.100.15/32
add burst-time=10s/10s comment=10001 limit-at=10200/41k max-limit=512k/2048k \
    name=SpLSTQ_1-1 parent=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.2/32
add burst-time=10s/10s comment=20002 limit-at=10200/41k max-limit=512k/2048k \
    name=SpLSTQ_2-2 parent=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.3/32
add burst-time=10s/10s comment=30003 limit-at=10200/41k max-limit=512k/2048k \
    name=SpLSTQ_3-3 parent=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.4/32
add burst-time=10s/10s comment=10004 limit-at=10200/41k max-limit=512k/2048k \
    name=SpLSTQ_4-4 parent=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.5/32
add burst-time=10s/10s comment=20005 limit-at=10200/41k max-limit=512k/2048k \
    name=SpLSTQ_5-5 parent=SpLSTG_0-1 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.6/32
add burst-time=10s/10s comment=30006 limit-at=20400/100k max-limit=1024k/5M \
    name=SpLSTQ_6-6 parent=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.7/32
add burst-time=10s/10s comment=10007 limit-at=20400/100k max-limit=1024k/5M \
    name=SpLSTQ_7-7 parent=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.8/32
add burst-time=10s/10s comment=20008 limit-at=20400/100k max-limit=1024k/5M \
    name=SpLSTQ_8-8 parent=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.9/32
add burst-time=10s/10s comment=30009 limit-at=20400/100k max-limit=1024k/5M \
    name=SpLSTQ_9-9 parent=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.10/32
add burst-time=10s/10s comment=40010 limit-at=20400/100k max-limit=1024k/5M \
    name=SpLSTQ_10-10 parent=SpLSTG_0-2 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.11/32
add burst-time=10s/10s comment=40011 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSTQ_11-11 parent=SpLSTG_0-3 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.12/32
add burst-time=10s/10s comment=50012 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSTQ_12-12 parent=SpLSTG_0-4 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.13/32
add burst-time=10s/10s comment=50013 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSTQ_13-13 parent=SpLSTG_0-4 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.14/32
add burst-time=10s/10s comment=50014 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSTQ_14-14 parent=SpLSTG_0-5 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.17/32
add burst-time=10s/10s comment=10015 limit-at=205k/205k max-limit=2048k/2048k \
    name=SpLSTQ_15-15 parent=SpLSTG_0-6 priority=5/5 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.15/32
add burst-time=10s/10s comment=10016 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSTQ_16-16 parent=SpLSTG_0-5 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.16/32
add burst-time=10s/10s comment=40017 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSTQ_17-17 parent=SpLSTG_0-5 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.18/32
add burst-time=10s/10s comment=30018 limit-at=205k/1024k max-limit=\
    2048k/10240k name=SpLSTQ_18-18 parent=SpLSTG_0-5 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.19/32
add burst-time=10s/10s comment=20019 limit-at=205k/519k max-limit=2048k/5192k \
    name=SpLSTQ_19-19 parent=SpLSTG_0-4 priority=1/1 queue=\
    pcq-download-default/pcq-upload-default target=192.168.100.24/32
