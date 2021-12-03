# net-useful
Useful Splynx, Mikrotik router OS and Linux scripts

BTEST is a tcp bandwidth test for unix platforms. It can analyze TCP dump file that grabbed statistics from interface during the data transfer. 
The result shows the bandwidth usage of each single TCP session, it's duration and data transferred as well as the overall statistics

GEO-IP is a tool to check how IP address (the whole /24 network) is displayed in top geo ip databases. Also it displays the data from whois database, that is based on RIR database.

MK CONFIGS folder has different Mikrotik configurations for queues

SPL SCRIPTS has few useful scripts that work with SPLYNX API:
- ppp-mikrotik takes all Internet services from splynx and exports usernames and passwords to mikrotik PPP secrets configuration. 
- netstats.py is a script that is used to get the usage for selected period per /24 network. It takes all statistics of customers and aggregates them in the /24 networks. Useful for designing and playing with BGP load balancing. 

