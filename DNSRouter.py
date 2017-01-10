"""
DNSRouter

This software is licensed under the Apache 2 license, quoted below.

Copyright 2017 Aniruddha Thombre <aniruddha at aniruddhas dot com, twitter: @imagineers7> 

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.

"""

from optparse import OptionParser,OptionGroup
import yaml
import sys
import re
from twisted.internet import reactor, defer
from twisted.names import client, dns, error, server
from twisted.python import log
from pyroute2 import IPRoute,netlink
log.startLogging(sys.stdout)
log.msg('Started logger for custom DNS server')
import socket 
version = "0.1"
class DynamicResolver(object):
    """
    Resolve, query, change rules and respond.
    """
    _flag = False
    _records = ''
    _authority = ''
    _answers = ''
    _additional = ''
    _dev = ""
    _gw = ""
    _resolvconf = ""
    def __init__ (self,trappatterns,customdev,customgw,resolvconf):
        self.trappatterns = trappatterns
        self._dev = customdev
        self._gw = customgw
        self._resolvconf = resolvconf
        
        
        log.msg("Dynamic Resolver patterns ", "|".join(self.trappatterns) )
        jstring = "|".join(self.trappatterns)
        jstring = jstring.replace('"','')
        print jstring
        #self.recomp = re.compile("|".join(self.trappatterns))
        self.recomp = re.compile(jstring,re.IGNORECASE|re.VERBOSE|re.MULTILINE)
        #self.recomp = re.compile(jstring,re.VERBOSE | re.MULTILINE | re.IGNORECASE)
        log.msg("Dynamic Resolver patterns ", "|".join(self.trappatterns) )
    
    def _dynamicRoutingRequired(self, query):
        """
        Check the query to determine if a dynamic response is required.
        """
        queryname = query.name.name
        labels = query.name.name.split('.')
        log.msg('Query before match ' + queryname)
        log.msg('Query type is ',  query.type)

        
        if query.type == dns.A:        
            log.msg('Query type is A for ',  queryname, labels)
            if self.recomp.search(queryname):
                log.msg("searched against",queryname)
                log.msg("Dynamic routing required for query: ", queryname, " it matches: ", ",".join(self.trappatterns) )
                return True
#            if self.recomp.match(labels[0]):
#==============================================================================
#             if self.recomp.match(labels[0]):
#                 log.msg("###################################\n",labels[0],"\n################################\n")
#                 log.msg("Dynamic routing required for query: ", queryname, " it matches: ", ",".join(self.trappatterns) )
#                 return True
#              
#         return True
#==============================================================================
    def _addRoutes(self,ipaddress):
        log.msg("Adding route for ",ipaddress," using gw ",self._gw," and device ",self._dev)
        ip = IPRoute()
        devno = ip.link_lookup(ifname=self._dev)
        log.msg("Adding route for ",ipaddress," using gw ",self._gw," and device ",self._dev, "with dev no: ",devno)
        #ip.route("add", dst=ipaddress,mask=32,gateway=self._gw,oif=devno)
        try:
          ip.route("add", dst=ipaddress,mask=32,gateway=self._gw,oifname=self._dev)
        except netlink.NetlinkError as E:
          log.msg("Routing exception: ", E)
#netlink.NetlinkError
        
        
        
    def _doFormatResults(self,records,flags):
        answers, authority, additional = records
        print "printing something"
        print "records"
        print records
        print answers
        print authority
        print additional

            
#        print answers.paylod
#        print answers.name
        lines = ['# ' + "heading"]
        for a in answers:
            log.msg("working on ", a.name , 'flag is ',flags)
            if a.type == dns.A and flags:
                log.msg("working on ", a.name, " flag is set for this guy and is of type A")
            #    self._flag = False
                log.msg("dns query ", dns.QUERY_CLASSES.get(a.cls, 'UNKNOWN (%d)' % (a.cls,)))
                print socket.inet_ntop(socket.AF_INET, a.payload.address)
                IPAddress = socket.inet_ntop(socket.AF_INET, a.payload.address)
                log.msg("This ip address needs to be routed dynamically ",IPAddress)
                self._addRoutes(IPAddress)
            elif a.type == dns.CNAME and flags:
                log.msg("this is a CNAME record for me resetting flag")
                #self._flag = True
            #lines.append(' '.join(str(word) for word in line))
            
        print "done boss"
        self._answers = answers
        self._authority = authority
        self._additional = additional
    
        #print '\n'.join(line for line in lines)
        
        
        


    def _doDynamicResponse(self, query,flags):
        """
        Calculate the response to a query.
        """
        name = query.name.name
        labels = name.split('.')
#        lastOctet = int(parts[1])
        r = client.Resolver(self._resolvconf)
        log.msg("Looking up A record in dynamic Response for ",name)
      
        d = defer.gatherResults([r.lookupAddress(name).addCallback(self._doFormatResults,flags)])
        #return d
#==============================================================================
#         answer = dns.RRHeader(
#             name=name,
#             payload=dns.Record_A())
#         answers = [answer]
#         authority = []
#         additional = []
#==============================================================================
        answers = self._answers
        authority = self._authority
        additional = self._additional
        self._answers = self._authority = self._additional = ''
        print "returning answers, authority and additional"
        print answers
        print authority
        print additional
        return answers, authority, additional


    def query(self, query, timeout=None):
        """
        Check if the query should be answered dynamically, otherwise dispatch to
        the fallback resolver.
        """
        if self._dynamicRoutingRequired(query):
            #return defer.fail(error.DomainError())
            tmp = defer.succeed(self._doDynamicResponse(query,True))
            return defer.fail(error.DomainError())
        else:
     #       return defer.succeed(self._doDynamicResponse(query))        
            return defer.fail(error.DomainError())



def main():
    """
    Run the server.
    """
    header = "=================================================\n"
    header += "                                                 \n"
    header += " ____  _   _ ____  ____              _           \n"
    header += "|  _ \| \ | / ___||  _ \ ___  _   _| |_ ___ _ __ \n"
    header += "| | | |  \| \___ \| |_) / _ \| | | | __/ _ \ '__|\n"
    header += "| |_| | |\  |___) |  _ < (_) | |_| | ||  __/ |   \n"
    header += "|____/|_| \_|____/|_| \_\___/ \__,_|\__\___|_|   \n"
    header += "                         Version: " + version + "            \n"
    header += "Home:    https://github.com/aniruddhas/DNSrouter \n"
    header += "By: Aniruddha Thombre, Twitter: @imagineers       \n"
    header += "=================================================\n"
    
    parser = OptionParser(usage = "dtrouter.py [options]:\n" + header, description="DT Router is supposed to work in controlled environment." )
    optgroup = OptionGroup(parser, "Route Dynamically")
    rngroup = OptionGroup(parser, "runtime options")
    optgroup.add_option('--file','-f', action="store", help="Specify a file containing configuration details. Config data from file overrides config options")
    parser.add_option_group(optgroup)
    rngroup.add_option("-p","--port", action="store", metavar="10054", type="int", default="10054", help='Listen on port, default is 10054')
    rngroup.add_option("-g","--gw", action="store", metavar="123.236.184.1", default="123.236.184.1", help='Gateway for trapped patterns')
    rngroup.add_option("-d","--dev", action="store", metavar="eth2", default="eth2", help='Ethernet device for trapped IPs')
    rngroup.add_option("-r","--res", action="store", metavar="/etc/resolv.conf", default="/etc/resolv.conf", help='resolv.conf to be used')

    rngroup.add_option("-q", "--quiet", action="store_false", dest="verbose", default=True, help="Go silent, Crickets!")
    parser.add_option_group(rngroup)
    (options,args) = parser.parse_args()
    listenport = options.port
    customdev = options.dev
    customgw = options.gw
    resolvconf = options.res
    log.msg('DNS Router Listening on: ' , options.port)
    log.msg("Gateway Device is: ", customdev)
    log.msg("Gateway is ", customgw)
    log.msg("resolvconf is ", resolvconf)
    if options.verbose:
        print header
        
    if options.file:
        log.msg("Config file is provided ", options.file)
        with open (options.file,'r') as configfile:
            config = yaml.load(configfile)
            listenport = config["dnsconfig"]["port"]
            customgw = config["dnsconfig"]["customgw"]
            customdev = config["dnsconfig"]["customdev"]
            resolvconf = config["dnsconfig"]["resolvconf"]
            log.msg("resolv.conf provided: ", resolvconf)
            log.msg("config dns port is ", listenport)
            trappatterns = config["patterns"]
            log.msg("Config file patterns are ", ",".join(trappatterns) )
            
    
    factory = server.DNSServerFactory(
        clients=[DynamicResolver(trappatterns,customdev,customgw,resolvconf), client.Resolver(resolv=resolvconf)]
    )

    protocol = dns.DNSDatagramProtocol(controller=factory)
    log.msg('Started listening on ' , listenport)
    reactor.listenUDP(listenport, protocol)
    reactor.listenTCP(listenport, factory)

    reactor.run()



if __name__ == '__main__':
    raise SystemExit(main())


