# -*- coding: UTF8 -*-
import os,wmi

wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
objNicConfig = colNicConfigs[0]

def Main():
    Choose =  input("""
=============Welcome to Switch IP on China Telecom=============
1.Switch IP from room 506
2.Switch IP from room 508
3.Switch IP from room 607
4.Switch IP from room 401
5.Switch IP from DingXiang room 411

Press AnyKey to Exit

Please choose :""")

    if Choose == '1':
        Room = "on room 506"
        SetIpAndGateway(['10.6.246.23'],['255.255.255.0'],['10.6.246.1'],Room)
        SetDNS(['10.5.22.66','10.5.22.67'],Room)

    elif Choose == '2':
        Room = "on room 508"
        SetIpAndGateway(['10.6.246.110'],['255.255.255.192'],['10.6.246.65'],Room)
        SetDNS(['10.5.22.66','10.5.22.67'],Room)

    elif Choose == '3':
        Room = "on room 607"
        SetIpAndGateway(['10.6.228.10'],['255.255.255.128'],['10.6.228.1'],Room)
        SetDNS(['10.5.22.67'],Room)

    elif Choose == '4':
        Room = "on room 401"
        SetIpAndGateway(['10.6.246.85'],['255.0.0.0'],['10.6.246.1'],Room)
        SetDNS(['10.5.22.66','10.5.22.67'],Room)

    elif Choose == '5':
        Room = "on DingXiang room 411"
        SetIpAndGateway(['10.4.31.73'],['255.255.255.128'],['10.4.31.1'],Room)
        SetDNS(['10.5.22.66','10.5.22.67'],Room)

    else:
        print ("Bye~")
        exit(1)
    
def SetIpAndGateway(IP,Yanma,Gateway,Room):
    if len(colNicConfigs) < 1:
        print ("No available network adapters found!")
        exit()
    returnIPValue = objNicConfig.EnableStatic(IPAddress=IP, SubnetMask=Yanma)
    returnGatewayValue = objNicConfig.SetGateways(DefaultIPGateway=Gateway)

    if returnIPValue[0] == 0:
        print("Set IP and SubnetMask " + Room + " successfully!")
        print("The new IP address is:" + '  '.join(IP))
        print("The new SubnetMask address is:" + '  '.join(Yanma))
        print ("================================================")
    else:
        print ("Set IP and SubnetMask Fail!")

    if returnGatewayValue[0] == 0:
        print("Set Gateway " + Room + " successfully!")
        print("The new Gateway address is:" + '  '.join(Gateway))
        print ("================================================")
    else:
        print ("Set Gateway Fail!")

def SetDNS(DNSServers,Room):
    if len(colNicConfigs) < 1:
        print ("No available network adapters found!")
        exit()
    returnDNSValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=DNSServers)
    
    if returnDNSValue[0] == 0:
        print("Set DNS " + Room + " successfully!")
        print("The new DNS address is:" + '  '.join(DNSServers))
        print ("================================================")
    else:
        print ("Set DNS Fail!")
    os.system('IPCONFIG/FLUSHDNS')
    CountineOrExit()

def CountineOrExit():
    IsExit = input ("Countine(Y) or Exit(N)? ")
    while(1):
        if IsExit.upper() == 'Y':
            Main()
        elif IsExit.upper() == 'N':
            print("Bye~")
            exit(1)
        else:
            print("You have inputed illegal character,try again!")
            CountineOrExit()
            break   

if __name__ == '__main__':
    Main()
    
    
