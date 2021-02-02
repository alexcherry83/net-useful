Script that allows to check IP address information in most used GEO IP databases <br>

geo_ip class : connects to the RIR database to check what is the latest info of the IP address and the network.<br>
Separate class for maxmind connection and class for using REST API of 6 other most used geo ip databases<br>

please use pip install geo2ip to get maxmind module that is used to connect to it's webservice <br>
also IPWhois is used to get data from RIPE or other RIR databases (pip install ipwhois) <br>
