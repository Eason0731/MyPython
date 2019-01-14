# -*- coding: UTF8 -*-
import os,wmi

wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
objNicConfig = colNicConfigs[0]

def SetOnRoom401():
    if len(colNicConfigs) < 1:
        #print("没有找到可用的网络适配器")
        print ("No available network adapters found!")
        exit()
    IP = ['10.6.246.85']
    Yanma = ['255.0.0.0']
    Gateway = ['10.6.246.1']
    DNSServers = ['10.5.22.66','10.5.22.67']
    returnIPValue = objNicConfig.EnableStatic(IPAddress=IP, SubnetMask=Yanma)
    returnGatewayValue = objNicConfig.SetGateways(DefaultIPGateway=Gateway)
    returnDNSValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=DNSServers)

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

    if returnDNSValue[0] == 0:
        print("Set DNS successfully!")
        print("The new DNS address is:" + '  '.join(DNSServers))
        print ("================================================")
    else:
        print ("Set DNS Fail!")
    os.system('IPCONFIG/FLUSHDNS')

def SetOnRoom607():
    if len(colNicConfigs) < 1:
        #print("没有找到可用的网络适配器")
        print ("No available network adapters found!")
        exit()
    IP = ['10.6.228.10']
    Yanma = ['255.255.255.128']
    Gateway = ['10.6.228.1']
    DNSServers = ['10.5.22.67']
    returnIPValue = objNicConfig.EnableStatic(IPAddress=IP, SubnetMask=Yanma)
    returnGatewayValue = objNicConfig.SetGateways(DefaultIPGateway=Gateway)
    returnDNSValue = objNicConfig.SetDNSServerSearchOrder(DNSServerSearchOrder=DNSServers)

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

    if returnDNSValue[0] == 0:
        print("Set DNS successfully!")
        print("The new DNS address is:" + '  '.join(DNSServers))
        print ("================================================")
    else:
        print ("Set DNS Fail!")
    os.system('IPCONFIG/FLUSHDNS')

if __name__ == '__main__':
    #SetOnRoom401()
    SetOnRoom607()
    
