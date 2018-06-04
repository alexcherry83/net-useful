/queue tree
add max-limit=10M name=#ROOT parent=global queue=synchronous-default
add limit-at=512k max-limit=1M name=icmp packet-mark=icmp parent=#ROOT priority=1
add limit-at=256k max-limit=512k name=DNS packet-mark=dns parent=#ROOT priority=1
add limit-at=512k max-limit=2M name=VoIP packet-mark=sip parent=#ROOT priority=3
add limit-at=1M max-limit=10M name=SSL packet-mark=ssl parent=#ROOT priority=1 queue=synchronous-default
add limit-at=1M max-limit=10M name=WWW packet-mark=www parent=#ROOT priority=6 queue=default
add max-limit=5M name=MAIL packet-mark=mail parent=#ROOT
add max-limit=10M name=OTHER packet-mark=no-mark parent=#ROOT
add limit-at=256k max-limit=1M name=WINBOX packet-mark=winbox parent=#ROOT priority=2
add limit-at=1M max-limit=10M name=SpeedTest packet-mark=speedtest.net parent=#ROOT priority=4
add limit-at=2M max-limit=5M name=NetFLIX packet-mark=Netflix parent=#ROOT priority=4 queue=default
add limit-at=700k max-limit=1M name=BWTEST packet-mark=bwtest parent=#ROOT priority=1 queue=default