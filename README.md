# DNSrouter
A Simple Hack for Name / FQDN / DNS based IP routing 

Expected setup:

* DNSrouter sits on a Linux router
* Has required python libraries
* Client DNS queries are intercepted via iptables and sent to DNSrouter
or:
* Clients are configured to directly send queries to DNSrouter

Example configuration file is included

##Example command and output:


```
sudo python DNSRouter.py -f config2 
2017-01-10 17:40:32+0530 [-] Log opened.
2017-01-10 17:40:32+0530 [-] Started logger for custom DNS server
2017-01-10 17:40:32+0530 [-] DNS Router Listening on:  10054
2017-01-10 17:40:32+0530 [-] Gateway Device is:  eth2
2017-01-10 17:40:32+0530 [-] Gateway is  123.236.184.1
2017-01-10 17:40:32+0530 [-] resolvconf is  ./resolvconf
2017-01-10 17:40:32+0530 [-] =================================================
2017-01-10 17:40:32+0530 [-]                                                  
2017-01-10 17:40:32+0530 [-]  ____  _   _ ____  ____              _           
2017-01-10 17:40:32+0530 [-] |  _ \| \ | / ___||  _ \ ___  _   _| |_ ___ _ __ 
2017-01-10 17:40:32+0530 [-] | | | |  \| \___ \| |_) / _ \| | | | __/ _ \ '__|
2017-01-10 17:40:32+0530 [-] | |_| | |\  |___) |  _ < (_) | |_| | ||  __/ |   
2017-01-10 17:40:32+0530 [-] |____/|_| \_|____/|_| \_\___/ \__,_|\__\___|_|   
2017-01-10 17:40:32+0530 [-]                          Version: 0.1            
2017-01-10 17:40:32+0530 [-] Home:    https://github.com/aniruddhas/DNSrouter 
2017-01-10 17:40:32+0530 [-] By: Aniruddha Thombre, Twitter: @imagineers       
2017-01-10 17:40:32+0530 [-] =================================================
2017-01-10 17:40:32+0530 [-] 
2017-01-10 17:40:32+0530 [-] Config file is provided  config2
2017-01-10 17:40:32+0530 [-] resolv.conf provided:  ./resolv.conf
2017-01-10 17:40:32+0530 [-] config dns port is  10025
2017-01-10 17:40:32+0530 [-] Config file patterns are  whatismyip.org,whatsapp,airtel,facebook,fbcdn,youtube
2017-01-10 17:40:32+0530 [-] Dynamic Resolver patterns  whatismyip.org|whatsapp|airtel|facebook|fbcdn|youtube
2017-01-10 17:40:32+0530 [-] whatismyip.org|whatsapp|airtel|facebook|fbcdn|youtube
2017-01-10 17:40:32+0530 [-] Dynamic Resolver patterns  whatismyip.org|whatsapp|airtel|facebook|fbcdn|youtube
2017-01-10 17:40:32+0530 [-] ./resolv.conf changed, reparsing
2017-01-10 17:40:32+0530 [-] Resolver added ('8.8.8.8', 53) to server list
2017-01-10 17:40:32+0530 [-] Resolver added ('202.149.208.91', 53) to server list
2017-01-10 17:40:32+0530 [-] Resolver added ('202.149.208.92', 53) to server list
2017-01-10 17:40:32+0530 [-] Resolver added ('124.124.204.36', 53) to server list
2017-01-10 17:40:32+0530 [-] Resolver added ('115.254.108.244', 53) to server list
2017-01-10 17:40:32+0530 [-] Started listening on  10025
2017-01-10 17:40:32+0530 [-] DNSDatagramProtocol starting on 10025
2017-01-10 17:40:32+0530 [-] Starting protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a5fc990>
2017-01-10 17:40:32+0530 [-] DNSServerFactory starting on 10025
2017-01-10 17:40:32+0530 [-] Starting factory <twisted.names.server.DNSServerFactory instance at 0x7f7a2a606ef0>
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Query before match facebook.com
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Query type is  1
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Query type is A for  facebook.com ['facebook', 'com']
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] searched against facebook.com
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Dynamic routing required for query:  facebook.com  it matches:  whatismyip.org,whatsapp,airtel,facebook,fbcdn,youtube
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] ./resolv.conf changed, reparsing
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Resolver added ('8.8.8.8', 53) to server list
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Resolver added ('202.149.208.91', 53) to server list
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Resolver added ('202.149.208.92', 53) to server list
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Resolver added ('124.124.204.36', 53) to server list
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Resolver added ('115.254.108.244', 53) to server list
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Looking up A record in dynamic Response for  facebook.com
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] DNSDatagramProtocol starting on 4787
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Starting protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a5ee490>
2017-01-10 17:40:46+0530 [-] returning answers, authority and additional
2017-01-10 17:40:46+0530 [-] 
2017-01-10 17:40:46+0530 [-] 
2017-01-10 17:40:46+0530 [-] 
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] DNSDatagramProtocol starting on 25956
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Starting protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a599150>
2017-01-10 17:40:46+0530 [-] printing something
2017-01-10 17:40:46+0530 [-] records
2017-01-10 17:40:46+0530 [-] ([<RR name=facebook.com type=A class=IN ttl=185s auth=False>], [], [])
2017-01-10 17:40:46+0530 [-] [<RR name=facebook.com type=A class=IN ttl=185s auth=False>]
2017-01-10 17:40:46+0530 [-] []
2017-01-10 17:40:46+0530 [-] []
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] working on  facebook.com flag is  True
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] working on  facebook.com  flag is set for this guy and is of type A
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] dns query  IN
2017-01-10 17:40:46+0530 [-] 157.240.7.35
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] This ip address needs to be routed dynamically  157.240.7.35
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Adding route for  157.240.7.35  using gw  192.168.1.2  and device  eth1
2017-01-10 17:40:46+0530 [DNSDatagramProtocol (UDP)] Adding route for  157.240.7.35  using gw  192.168.1.2  and device  eth1 with dev no:  []
2017-01-10 17:40:46+0530 [-] done boss
2017-01-10 17:40:46+0530 [-] (UDP Port 25956 Closed)
2017-01-10 17:40:46+0530 [-] Stopping protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a599150>
2017-01-10 17:40:46+0530 [-] (UDP Port 4787 Closed)
2017-01-10 17:40:46+0530 [-] Stopping protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a5ee490>
^C2017-01-10 17:41:08+0530 [-] Received SIGINT, shutting down.
2017-01-10 17:41:08+0530 [twisted.names.server.DNSServerFactory] (TCP Port 10025 Closed)
2017-01-10 17:41:08+0530 [-] Stopping factory <twisted.names.server.DNSServerFactory instance at 0x7f7a2a606ef0>
2017-01-10 17:41:08+0530 [DNSDatagramProtocol (UDP)] (UDP Port 10025 Closed)
2017-01-10 17:41:08+0530 [DNSDatagramProtocol (UDP)] Stopping protocol <twisted.names.dns.DNSDatagramProtocol object at 0x7f7a2a5fc990>
2017-01-10 17:41:08+0530 [-] Main loop terminated.


```
