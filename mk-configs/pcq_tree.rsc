# apr/05/2018 14:20:17 by RouterOS 6.41.3
# software id = 
#
#
#
/queue tree
add limit-at=512 max-limit=5120 name=TEST_CUSTOMER_IN parent=global queue=\
    default
add limit-at=256 max-limit=1024 name=TEST_CUSTOMER_OUT parent=global queue=\
    default
add name=SpLMain_UP parent=global priority=5 queue=default
add name=SpLMain_DOWN parent=global priority=5 queue=default
add burst-time=10s limit-at=205k max-limit=2048k name=SpLPGroup_1-DOWN \
    packet-mark=SpLPGMark_1-in parent=SpLMain_DOWN priority=5 queue=\
    SpLPCQGroup_1-DOWN
add burst-time=10s limit-at=51k max-limit=512k name=SpLPGroup_1-UP \
    packet-mark=SpLPGMark_1-out parent=SpLMain_UP priority=5 queue=\
    SpLPCQGroup_1-UP
add burst-time=10s limit-at=500k max-limit=5M name=SpLPGroup_2-DOWN \
    packet-mark=SpLPGMark_2-in parent=SpLMain_DOWN priority=5 queue=\
    SpLPCQGroup_2-DOWN
add burst-time=10s limit-at=102k max-limit=1024k name=SpLPGroup_2-UP \
    packet-mark=SpLPGMark_2-out parent=SpLMain_UP priority=5 queue=\
    SpLPCQGroup_2-UP
add burst-time=10s limit-at=1024k max-limit=10240k name=SpLPGroup_3-DOWN \
    packet-mark=SpLPGMark_3-in parent=SpLMain_DOWN priority=5 queue=\
    SpLPCQGroup_3-DOWN
add burst-time=10s limit-at=205k max-limit=2048k name=SpLPGroup_3-UP \
    packet-mark=SpLPGMark_3-out parent=SpLMain_UP priority=5 queue=\
    SpLPCQGroup_3-UP
add burst-time=10s limit-at=1557k max-limit=15576k name=SpLPGroup_4-DOWN \
    packet-mark=SpLPGMark_4-in parent=SpLMain_DOWN priority=1 queue=\
    SpLPCQGroup_4-DOWN
add burst-time=10s limit-at=615k max-limit=6144k name=SpLPGroup_4-UP \
    packet-mark=SpLPGMark_4-out parent=SpLMain_UP priority=1 queue=\
    SpLPCQGroup_4-UP
add burst-time=10s limit-at=4096k max-limit=40960k name=SpLPGroup_5-DOWN \
    packet-mark=SpLPGMark_5-in parent=SpLMain_DOWN priority=1 queue=\
    SpLPCQGroup_5-DOWN
add burst-time=10s limit-at=820k max-limit=8192k name=SpLPGroup_5-UP \
    packet-mark=SpLPGMark_5-out parent=SpLMain_UP priority=1 queue=\
    SpLPCQGroup_5-UP
add burst-time=10s limit-at=205k max-limit=2048k name=SpLPGroup_6-DOWN \
    packet-mark=SpLPGMark_6-in parent=SpLMain_DOWN priority=5 queue=\
    SpLPCQGroup_6-DOWN
add burst-time=10s limit-at=205k max-limit=2048k name=SpLPGroup_6-UP \
    packet-mark=SpLPGMark_6-out parent=SpLMain_UP priority=5 queue=\
    SpLPCQGroup_6-UP
