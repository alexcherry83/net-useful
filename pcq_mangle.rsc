# apr/05/2018 14:20:02 by RouterOS 6.41.3
# software id = 
#
#
#
/ip firewall mangle
add action=mark-connection chain=prerouting comment=TEST_CUSTOMER \
    new-connection-mark=TEST_CUSTOMER passthrough=yes src-address=10.0.0.25
add action=mark-packet chain=prerouting connection-mark=TEST_CUSTOMER \
    new-packet-mark=TEST_CUSTOMER passthrough=no
add action=mark-connection chain=prerouting comment=TEST_CUSTOMER \
    dst-address=10.0.0.25 new-connection-mark=TEST_CUSTOMER_IN passthrough=\
    yes
add action=mark-packet chain=prerouting connection-mark=TEST_CUSTOMER_IN \
    new-packet-mark=TEST_CUSTOMER_IN passthrough=no
add chain=input comment="Splynx start mangle" disabled=yes src-address=\
    0.0.0.0
add action=mark-packet chain=postrouting comment=SpLPGMark_1-in \
    dst-address-list=SpLAL_1 new-packet-mark=SpLPGMark_1-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_1-out new-packet-mark=\
    SpLPGMark_1-out passthrough=no src-address-list=SpLAL_1
add action=mark-packet chain=postrouting comment=SpLPGMark_2-in \
    dst-address-list=SpLAL_2 new-packet-mark=SpLPGMark_2-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_2-out new-packet-mark=\
    SpLPGMark_2-out passthrough=no src-address-list=SpLAL_2
add action=mark-packet chain=postrouting comment=SpLPGMark_3-in \
    dst-address-list=SpLAL_3 new-packet-mark=SpLPGMark_3-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_3-out new-packet-mark=\
    SpLPGMark_3-out passthrough=no src-address-list=SpLAL_3
add action=mark-packet chain=postrouting comment=SpLPGMark_4-in \
    dst-address-list=SpLAL_4 new-packet-mark=SpLPGMark_4-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_4-out new-packet-mark=\
    SpLPGMark_4-out passthrough=no src-address-list=SpLAL_4
add action=mark-packet chain=postrouting comment=SpLPGMark_5-in \
    dst-address-list=SpLAL_5 new-packet-mark=SpLPGMark_5-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_5-out new-packet-mark=\
    SpLPGMark_5-out passthrough=no src-address-list=SpLAL_5
add action=mark-packet chain=postrouting comment=SpLPGMark_6-in \
    dst-address-list=SpLAL_6 new-packet-mark=SpLPGMark_6-in passthrough=no
add action=mark-packet chain=forward comment=SpLPGMark_6-out new-packet-mark=\
    SpLPGMark_6-out passthrough=no src-address-list=SpLAL_6
add chain=input comment="Splynx end mangle" disabled=yes src-address=0.0.0.0
