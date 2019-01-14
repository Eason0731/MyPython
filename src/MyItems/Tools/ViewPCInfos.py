import os
import getpass
import socket
import uuid
import platform
import re,urllib.request,urllib.error,urllib.parse,requests
from subprocess import Popen, PIPE
import FileOperation

def ViewPCInfos():
    output = os.popen('pip list')
    if 'WMI' not in output.read():
        os.system('pip install wmi')
    pcname = socket.getfqdn(socket.gethostname())
    currentusername = getpass.getuser()
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]  
    mac_address = "-".join([mac[e:e+2] for e in range(0,11,2)])
    n_ip = re.search('\d+\.\d+\.\d+\.\d+',str(Popen('ipconfig', stdout=PIPE).stdout.read())).group(0) #Add a str here to suit on python3
    print("=====================PC Infos======================")
    os_version()
    cpu_mem() 
    disk()
    print("PC name: " + pcname)
    print("Current login user: " + currentusername)
    print("Intranet IP: " + n_ip)
    print("Public network IP: " + GetPublicNetworkIP())
    print("Mac address: " + mac_address)
    print("===================================================")
    FileOperation.CountineOrExit()

def GetPublicNetworkIP():
    import re,urllib.request,urllib.error,urllib.parse
    try:
        ipURL = requests.get("http://txt.go.sohu.com/ip/soip").text #'http://txt.go.sohu.com/ip/soip' This site is available to search IP
        publicip = re.findall(r'\d+.\d+.\d+.\d+',ipURL) #use findall regular to find public network ip
    except Exception as e:
        publicip = str(e)
    return publicip[0]

def os_version():
    import platform
    import wmi
    c = wmi.WMI ()
    print("OS name and version: " + platform.platform())
    for sys in c.Win32_OperatingSystem(): 
        #print("Bits: " + sys.OSArchitecture.encode("UTF8"))
        print("Bits: " + str(sys.OSArchitecture)) #sys.OSArchitecture should be changed to string type on python3
        print("Current process count: " + str(sys.NumberOfProcesses))
    print("       ")

def cpu_mem():
    import wmi
    c = wmi.WMI ()         
    for processor in c.Win32_Processor(): 
        print("Process Name: %s" % processor.Name.strip()) 
    for Memory in c.Win32_PhysicalMemory(): 
        print("Memory Capacity: %.fMB" %(int(Memory.Capacity)/1048576))
    print("       ")

def disk():
    import wmi
    c = wmi.WMI ()    
    for physical_disk in c.Win32_DiskDrive (): 
        for partition in physical_disk.associators ("Win32_DiskDriveToDiskPartition"): 
            for logical_disk in partition.associators ("Win32_LogicalDiskToPartition"): 
                print(physical_disk.Caption.encode("UTF8"), partition.Caption.encode("UTF8"), logical_disk.Caption) 
    print("       ")
   
    for disk in c.Win32_LogicalDisk (DriveType=3): 
        print(disk.Caption, "%0.2f%% free" % (100.0 * int (disk.FreeSpace) / int (disk.Size))) 
    print("       ")

if __name__ == '__main__':
    ViewPCInfos()
