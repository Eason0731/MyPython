# -*- coding: UTF8 -*-
import os,wmi

wmiService = wmi.WMI()
colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
objNicConfig = colNicConfigs[0]

def SetIPandDNS(IP,Yanma,Gateway,DNSServers):
    if len(colNicConfigs) < 1:
        #print("没有找到可用的网络适配器")
        print ("No available network adapters found!")
        exit()
    
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
    SetIPandDNS(['10.6.228.10'],['255.255.255.128'],['10.6.228.1'],['10.5.22.67'])
    #SetIPandDNS(['10.6.246.85'],['255.0.0.0'],['10.6.246.1'],['10.5.22.66','10.5.22.67'])
    
