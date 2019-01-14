# -*- coding: UTF8 -*-
import os,wmi

wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
objNicConfig = colNicConfigs[0]

def ManualSetIpAndGateway():
    if len(colNicConfigs) < 1:
        #print("没有找到可用的网络适配器")
        print ("No available network adapters found!")
        exit()
    IP = ['192.168.1.88']
    Yanma = ['255.255.255.0']
    Gateway = ['192.168.1.1']
    returnIPValue = objNicConfig.EnableStatic(IPAddress=IP, SubnetMask=Yanma)
    returnGatewayValue = objNicConfig.SetGateways(DefaultIPGateway=Gateway)

    if returnIPValue[0] == 0:
        print("Set IP and SubnetMask successfully!")
        print("The new IP address is:" + '  '.join(IP))
        print("The new SubnetMask address is:" + '  '.join(Yanma))
        print ("================================================")
    else:
        print ("Set IP and SubnetMask Fail!")

    if returnGatewayValue[0] == 0:
        print("Set Gateway successfully!")
        print("The new Gateway address is:" + '  '.join(Gateway))
        print ("================================================")
    else:
        print ("Set Gateway Fail!")

def ManualSetDNS():
    if len(colNicConfigs) < 1:
        print ("No available network adapters found!")
        exit()
    DNSServers = ['223.5.5.5','223.6.6.6']
    returnDNSValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=DNSServers)
    
    if returnDNSValue[0] == 0:
        print("Set DNS successfully!")
        print("The new DNS address is:" + '  '.join(DNSServers))
        print ("================================================")
    else:
        print ("Set DNS Fail!")
    os.system('IPCONFIG/FLUSHDNS')

def AutoSetIpAndGateway():
    if len(colNicConfigs) < 1:
        print ("No available network adapters found!")
        exit()
    returnIPValue = objNicConfig.EnableDHCP()
    if returnIPValue[0] == 0:
        print ('Set random IP and Gateway successfully!')
        print ("================================================")

def AutoSetDNS():
    if len(colNicConfigs) < 1:
        print ("No available network adapters found!")
        exit()
    DNSServers = []
    returnDNSValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=DNSServers)
    if returnDNSValue[0] == 0 :
        print ('Set random DNS successfully!')
        print ("================================================")
    os.system('IPCONFIG/FLUSHDNS')

if __name__ == '__main__':
    #ManualSetIpAndGateway()
    AutoSetIpAndGateway()
    ManualSetDNS() 
    #AutoSetDNS()
    
