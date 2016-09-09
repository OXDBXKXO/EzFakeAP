#!/usr/bin/python
'''
Author: FATGEEK 
Contact: fatgeek@gmail.com
Description: Little script that helps you creating a fake access point
Version: 0.1 "Just getting the script working, enhancments are coming ;)"
'''

### Jump Index
#jump 0 : Welcome Menu, choosing the Fake AP Mode
#jump 1 : Choosing the target of the Evil Twin Attack
#jump 2 : Setting up the DHCP Server
#jump 3 : Setting up the Karma-Attack AP
#jump 4 : Creating dnsmasq config file
#jump 5 : Choosing the interface to put into monitor mode
#jump 6 : Setting up the ESSID
#jump 7 :


#Getting ready
from os import system
from time import sleep as slp
import ERfonctions as mod
import subprocess as sp

#Variables
waitincrement = 0
jump = 2
choicemade = 0
Refresh = 0

#Message Display
ask =          "        [" + mod.colors.YELLOW + "?" + mod.colors.DEFAULT + "] "
info =         "        [" + mod.colors.LGREEN + "*" + mod.colors.DEFAULT + "] "
answer =    "           [" + mod.colors.LCYAN  + ">" + mod.colors.DEFAULT + "] "
error =     "           [" + mod.colors.LRED   + "!" + mod.colors.DEFAULT + "] "
errorsoft = "           [" + mod.colors.YELLOW + "!" + mod.colors.DEFAULT + "] "

#Config Infos
MODE      = "Not Configured"
MONITOR   = "Not Configured"
DHCPStart = "Not Configured"
DHCPStop  = "Not Configured"
DNS       = "Not Configured"
ESSID     = "Not Configured"
CHANNEL   = "Not Configured"
PASS      = "Not Configured"
STATUS    = "Inactive"

def InfosHeader():
    system('clear')
    #Printing informations about the config of the AP
    print(mod.colors.LGREEN + "\n                ************************************" + mod.colors.DEFAULT)
    print(mod.colors.LCYAN +"                    EasyRogue v0.1 Configuration\n" + mod.colors.DEFAULT)
    print("                    Fake AP Mode : " + mod.colors.LRED + MODE + mod.colors.DEFAULT)
    print("                    Monitor Card : " + mod.colors.LRED + MONITOR + mod.colors.DEFAULT)
    print("                    ESSID        : " + mod.colors.LRED + ESSID + mod.colors.DEFAULT)
    print("                    Channel      : " + mod.colors.LRED + CHANNEL + mod.colors.DEFAULT)
    print("                    Password     : " + mod.colors.LRED + PASS + mod.colors.DEFAULT)
    print("                    DHCP Start   : " + mod.colors.LRED + DHCPStart + mod.colors.DEFAULT)
    print("                    DHCP Stop    : " + mod.colors.LRED + DHCPStop + mod.colors.DEFAULT)
    print("                    DNS Server   : " + mod.colors.LRED + DNS + mod.colors.DEFAULT)
    print("                    Status       : " + mod.colors.LRED + STATUS + mod.colors.DEFAULT)
    print(mod.colors.LGREEN + "\n                ***********************************\n" + mod.colors.DEFAULT)

while jump == 0:
    ################Choose the Ap Mode
    mod.WelcomeHeader()
    if (waitincrement == 0):
        slp(1)
        waitincrement = 1
        
    print("\n" + info + "There are three ways to create a Rogue Access Point :")
    print(mod.colors.BLUE + "\n            1" + mod.colors.DEFAULT + ") Evil Twin Access Point")
    print(mod.colors.BLUE + "\n            2" + mod.colors.DEFAULT + ") Honey Pot")
    print(mod.colors.BLUE + "\n            3" + mod.colors.DEFAULT + ") Karma-Attack Access Point")

    print("\n"+ ask +"Which one do you want to use ? \n")
    APWay = raw_input(answer)
    try:
        APWay = int(APWay)
    except:
        print("\n"+ error + "Invalide answer !")
        slp(2)
        continue
    
    ################Choice 
    
    if (APWay == 1):
            #INSERT EVIL TWIN HERE
            #AIRPLAY-NG, HOSTAPD, etc...
        print("\n"+error+"This part is not finished yet...")
        slp(2)
        continue
    
    elif (APWay == 3):
            #INSERT KARMA ATTACK HERE
        print("\n"+error+"This part is not finished yet...")
        slp(2)
        continue
    
    elif APWay == 2:
        choicemade = 2  #Set the mode
        MODE = mod.VariableColoring("G","Honey Pot")
        jump = 2        #Set where to go now
        break
    
    else:
        print("\n"+error+"] Invalide answer !")
        slp(2)
        continue
    
    
while jump == 2:
    ################Setting up DHCP
    exit_the_loop = 0
    InfosHeader()
    if Refresh == 0:
        print(""+ ask+"Starting DHCP address (ex: 10.0.0.50) ?\n")
        DHCPStart = mod.VariableColoring("G",raw_input(answer))
        Refresh = 1
        continue
    elif Refresh == 1:
        print(""+ ask+"Stopping DHCP address (ex: 10.0.0.150) ?\n")
        DHCPStop = mod.VariableColoring("G",raw_input(answer))
        Refresh = 2
        continue
    while exit_the_loop == 0:
        InfosHeader()
        print(""+ask+"Do you confirm these settings ? Y/n\n")
        confirm=raw_input(answer)
        if confirm == "y" or confirm == "Y":
            jump = 4
            exit_the_loop = 1
            break
        elif confirm == "n" or confirm == "N":
            DHCPStart = mod.VariableColoring("R","Not Configured")
            DHCPStop = mod.VariableColoring("R","Not Configured")
            Refresh = 0
            break
        else:
            print("\n"+error + "Invalide Answer !")
            slp(2)
            continue
    if exit_the_loop == 0:
        continue
        Refresh = 0
    else:
        Refresh = 0
        break
    
    
while jump == 4:
    ################Create the dnsmasq config file
    f = open('dnsmasq.conf', 'w')
    f.write('interface=at0\n' +
    'dhcp-range='+ DHCPStart + ',' + DHCPStop + ',12h\n' +
    'server=80.67.169.12\n' +
    'server=80.67.169.40\n')    #These DNSs do not log your web-activity
    f.close()
    system('dnsmasq -C dnsmasq.conf')
    jump = 5
    break


while jump == 5:
    ################Set up the monitor card
    exit_the_loop = 0
    InfosHeader()
    if Refresh == 0:
        print("" + ask +"Wireless interface to put into monitor mode ? (ex: wlan1)\n")
        MONITOR = mod.VariableColoring("G", raw_input(answer))
        Refresh = 1
        continue
    while exit_the_loop == 0:
        InfosHeader()
        print(""+ask+"Do you confirm this setting ? Y/n\n")
        confirm=raw_input(answer)
        if confirm == "y" or confirm == "Y":
            jump = 6
            exit_the_loop = 1
            break
        elif confirm == "n" or confirm == "N":
            MONITOR = mod.VariableColoring("R", "Not Configured")
            Refresh = 0
            break
        else:
            print("\n"+error + "Invalide Answer !")
            slp(2)
            continue
    if exit_the_loop == 0:
        continue
        Refresh = 0
    else:
        break
    
while jump == 6:
    ############Now setting up ESSID of the fake AP
    exit_the_loop = 0
    InfosHeader()
    if Refresh == 0:
        print("" + ask +"ESSID to broadcast ? (ex: FreeWifi)\n")
        ESSID = mod.VariableColoring("G", raw_input(answer))
        Refresh = 1
        continue
    while exit_the_loop == 0:
        InfosHeader()
        print(""+ask+"Do you confirm this setting ? Y/n\n")
        confirm=raw_input(answer)
        if confirm == "y" or confirm == "Y":
            jump = 7
            exit_the_loop = 1
            break
        elif confirm == "n" or confirm == "N":
            ESSID = mod.VariableColoring("R", "Not Configured")
            Refresh = 0
            break
        else:
            print("\n"+error + "Invalide Answer !")
            slp(2)
            continue
    if exit_the_loop == 0:
        continue
        Refresh = 0
    else:
        break

while jump == 7:
    ############Now setting up channel of emmission of the fake AP
    exit_the_loop = 0
    InfosHeader()
    if Refresh == 0:
        print("" + ask +"Channel to emit on ? (1-11)\n")
        CHANNEL = mod.VariableColoring("G", raw_input(answer))
        Refresh = 1
        continue
    while exit_the_loop == 0:
        InfosHeader()
        print(""+ask+"Do you confirm this setting ? Y/n\n")
        confirm=raw_input(answer)
        if confirm == "y" or confirm == "Y":
            jump = 7
            exit_the_loop = 1
            break
        elif confirm == "n" or confirm == "N":
            CHANNEL = mod.VariableColoring("R", "Not Configured")
            Refresh = 0
            break
        else:
            print("\n"+error + "Invalide Answer !")
            slp(2)
            continue
    if exit_the_loop == 0:
        continue
        Refresh = 0
    else:
        break


system('airmon-ng start ' + interface)
print "Now launching \"airbase-ng --essid %s mon0\"" % ssid
system('airbase-ng --essid %s mon0 &>/dev/null &' % ssid)

#Enable the at0 interface
ip = starter.split('.')
at_ip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.1'
system ('ifconfig at0 ' + at_ip + ' up netmask 255.255.255.0')

#Now set up IPv4 Forwarding
print "Making sure IPv4 forwarding is enabled..."
system('echo \'1\' > /proc/sys/net/ipv4/ip_forward')

#Now set up IPTables to be NAT
print "almost done..."
interwebz = raw_input("Enter the interface connected to the Interwebz (e.g. eth0)\n--> ")
print "working some IPtables...I hate IPtables..."
system('iptables --flush')
system('iptables --table nat --flush')
system('iptables --delete-chain')
system('iptables --table nat --delete-chain')
system('iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE' % interwebz)
system('iptables --append FORWARD --in-interface '+ interface +' -j ACCEPT')

print "%s should be broadcasting, now go forth and profit" % ssid
