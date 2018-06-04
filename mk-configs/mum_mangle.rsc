/ip firewall mangle
add action=mark-connection chain=prerouting comment=ICMP connection-mark=no-mark new-connection-mark=icmp \
    passthrough=yes protocol=icmp
add action=mark-packet chain=prerouting connection-mark=icmp new-packet-mark=icmp passthrough=no
add action=mark-connection chain=prerouting comment=DNS connection-mark=!dns dst-port=53 log-prefix=DNS \
    new-connection-mark=dns passthrough=yes protocol=udp
add action=mark-connection chain=output connection-mark=!dns dst-port=53 log-prefix=DNS new-connection-mark=\
    dns passthrough=yes protocol=udp
add action=mark-packet chain=prerouting connection-mark=dns new-packet-mark=dns passthrough=no
add action=mark-packet chain=output connection-mark=dns new-packet-mark=dns passthrough=no
add action=mark-connection chain=input comment=WINBOX dst-port=8291 new-connection-mark=winbox passthrough=\
    yes protocol=tcp
add action=mark-connection chain=output new-connection-mark=winbox passthrough=yes protocol=tcp src-port=8291
add action=mark-packet chain=input connection-mark=winbox new-packet-mark=winbox passthrough=no
add action=mark-packet chain=output connection-mark=winbox new-packet-mark=winbox passthrough=no
add action=mark-connection chain=prerouting comment=BWTEST dst-address=100.100.100.100 new-connection-mark=\
    bwtest passthrough=yes
add action=mark-packet chain=prerouting connection-mark=bwtest new-packet-mark=bwtest passthrough=no
add action=mark-connection chain=prerouting comment=SpeedTest content=speedtest.net new-connection-mark=\
    speedtest.net passthrough=yes protocol=tcp
add action=add-dst-to-address-list address-list=speedtest.net address-list-timeout=1h chain=prerouting \
    comment=SpeedTest disabled=yes dst-address-list=!NET-Privadas dst-port=8081,8080 protocol=tcp
add action=mark-packet chain=prerouting connection-mark=speedtest.net new-packet-mark=speedtest.net \
    passthrough=no
add action=mark-connection chain=prerouting comment=NetFLIX dst-address-list=Netflix new-connection-mark=\
    Netflix passthrough=yes
add action=mark-packet chain=prerouting connection-mark=Netflix new-packet-mark=Netflix passthrough=no
add action=mark-connection chain=prerouting comment=VoIP dst-port=5060-5070 new-connection-mark=sip \
    passthrough=yes protocol=udp
add action=mark-packet chain=prerouting connection-mark=sip new-packet-mark=sip passthrough=no
add action=mark-connection chain=prerouting comment=SSL connection-mark=!ssl dst-port=443 log-prefix=SSL \
    new-connection-mark=ssl passthrough=yes protocol=tcp
add action=mark-connection chain=prerouting comment=SSL connection-mark=!ssl dst-port=22 log-prefix=SSL \
    new-connection-mark=ssl passthrough=yes protocol=tcp
add action=mark-connection chain=prerouting comment=SSL connection-mark=!ssl dst-port=443 log-prefix=SSL \
    new-connection-mark=ssl passthrough=yes protocol=udp
add action=mark-packet chain=prerouting connection-mark=ssl new-packet-mark=ssl passthrough=no
add action=mark-connection chain=prerouting comment=WWW connection-mark=!www dst-port=80,5222-5228 \
    new-connection-mark=www passthrough=yes protocol=tcp
add action=mark-packet chain=prerouting connection-mark=www new-packet-mark=www passthrough=no
add action=mark-connection chain=prerouting comment=MAIL connection-mark=!mail dst-port=\
    25,110,993,143,465,587 log-prefix=Mail--- new-connection-mark=mail passthrough=yes protocol=tcp
add action=mark-packet chain=prerouting connection-mark=mail new-packet-mark=mail passthrough=no
add action=mark-connection chain=prerouting comment=OTHER connection-mark=no-mark new-connection-mark=\
    resto_trafico passthrough=yes
add action=mark-packet chain=prerouting connection-mark=resto_trafico disabled=yes new-packet-mark=\
    resto_trafico passthrough=no
