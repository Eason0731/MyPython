#coding=utf-8 
import os
import shutil
import time

def MainMethod(sourceOutlook,sourceMicrosoftOutlook):
    Choose = input("""
=========Welcome to Backup Archive Files===========
1. Backup Outlook Files
2. Put back Outlook Files
===================================================
Press AnyKey to Exit

Please Choose:""")
    if Choose == '1':
        Backup(sourceOutlook,sourceMicrosoftOutlook)
    elif Choose == '2':
        PutBack(sourceOutlook,sourceMicrosoftOutlook)
    else:
        exit(0)
    
def Backup(sourceOutlook,sourceMicrosoftOutlook):
    IsBackup = '1'
    BackupFolder = "BackupMyOutlook"
    BackupFolder = os.path.join("D:\\",BackupFolder)
    if os.path.exists(BackupFolder):
        shutil.rmtree(BackupFolder)
        print("Old backup folder: " + BackupFolder +" has been deleted successfully!")
        print("                                ")
    os.makedirs(BackupFolder)
    print("Create backup folder: " + BackupFolder + " successfully!")
    print("===================================================")
    MyFiles(sourceOutlook,sourceMicrosoftOutlook,BackupFolder,IsBackup)
    print("===================================================")
    ExitOrNot()
        
def MyFiles(sourceOutlook,sourceMicrosoftOutlook,BackupFolder,IsBackup):
    print(time.strftime("Start time :%Y-%m-%d %X",time.localtime()))
    Info = "'s archive files on this PC"
    if IsBackup == '1':
        if os.path.exists(sourceOutlook):
            Outlook(sourceOutlook,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Outlook" + Info)
        print("                                ")

        if os.path.exists(sourceMicrosoftOutlook):
            MicrosoftOutlook(sourceMicrosoftOutlook,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Microsoft Outlook" + Info)
        print("                                ")

    else:
        i = 0
        if os.path.exists(os.path.join(BackupFolder,'Outlook 文件')):
            i = i + 1   
            if not os.path.exists(sourceOutlook):
                Outlook(sourceOutlook,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Outlook " + sourceOutlook + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'Microsoft','Outlook')):
            i = i + 1   		
            if not os.path.exists(sourceMicrosoftOutlook):
                MicrosoftOutlook(sourceMicrosoftOutlook,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Microsoft Outlook " + sourceMicrosoftOutlook + " had existed")
            print("                                ")

        if i == 0:
            print(BackupFolder + " does not contain any releated backup files, this may not a correct backup folder")
        
    DeleteBackupFolder(BackupFolder,IsBackup)
    print(time.strftime("End time :%Y-%m-%d %X",time.localtime()))

def Outlook(sourceOutlook,BackupFolder,IsBackup):
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Outlook 文件')
        os.makedirs(BackupFolder)
        copyFiles(sourceOutlook,BackupFolder)
        print("Backup Outlook successfully! --- %.2f" % GetSize(sourceOutlook), "MB")
    else:
        shutil.move(os.path.join(BackupFolder,"Outlook 文件"), sourceOutlook)
        print("Put back Outlook successfully!")

def MicrosoftOutlook(sourceMicrosoftOutlook,BackupFolder,IsBackup):		
     if IsBackup == '1':		
         BackupFolder = os.path.join(BackupFolder,'Microsoft','Outlook')		
         os.makedirs(BackupFolder)		
         copyFiles(sourceMicrosoftOutlook,BackupFolder)		
         print("Backup Microsoft Outlook successfully! --- %.2f" % GetSize(sourceMicrosoftOutlook), "MB")		
     else:		
         shutil.move(os.path.join(BackupFolder,"Microsoft",'Outlook'), sourceMicrosoftOutlook)		
         if not os.listdir(os.path.join(BackupFolder,"Microsoft")):		
             shutil.rmtree(os.path.join(BackupFolder,"Microsoft"))		
         print("Put back Microsoft Outlook successfully!")
        
def PutBack(sourceOutlook,sourceMicrosoftOutlook):
    BackupFolder = "BackupMyOutlook"
    BackupFolder = os.path.join("D:\\",BackupFolder)
    print("===================================================")
    if os.path.exists(BackupFolder):
        IsBackup = '2'
        MyFiles(sourceOutlook,sourceMicrosoftOutlook,BackupFolder,IsBackup)
    else:
        print(BackupFolder + " is not exists!")
    print("===================================================")
    ExitOrNot()

def DeleteBackupFolder(BackupFolder,IsBackup):
    if not os.listdir(BackupFolder):
        shutil.rmtree(BackupFolder)
        if not os.path.exists(BackupFolder):
            if IsBackup == '1':
                print ("Empty archive files backup folder " + BackupFolder + " has been deleted successfully!")
            else:
                print("All archive files have been put back")
                print("Backup folder " + BackupFolder + " has been deleted successfully!")
                print("                                ")

def ExitOrNot():
    while(True):
        cc = input("Back to main menu? (Y/N)")
        if cc.lower() == 'y':
            MainMethod(sourceOutlook,sourceMicrosoftOutlook)
            break
        elif cc.lower() == 'n':
            exit(0)
        else:
            print("You've typed a illgeal word, please select again!")
            print("===================================================")    
     
def copyFiles(sourceDir, targetDir): 
    if sourceDir.find(".svn") > 0: 
        return 
    
    files = []
    i = 0
    while(1):
        try:
            files = os.listdir(sourceDir)
            break
        except OSError as e:
            print(e)
            if i >= 10:
                raise Exception('Cannot connect to resource more than 10 times: ' + '"' + sourceDir + '"')
            i = i + 1
            time.sleep(2)
        
    for file in files: 
        sourceFile = os.path.join(sourceDir, file) 
        targetFile = os.path.join(targetDir, file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            copyFiles(sourceFile, targetFile)

def GetSize(Source):  
   size = 0
   for root, dirs, files in os.walk(Source):
       for names in files:
           myfiles = os.path.join(root,names)
           size += sum([os.path.getsize(myfiles)])
   return (size/1024.00/1024.00)

if __name__ == "__main__":
    sourceOutlook = os.path.join(os.environ['USERPROFILE'],'Documents','Outlook 文件')    
    sourceMicrosoftOutlook = os.path.join(os.environ['localappdata'],'Microsoft','Outlook')
    
    MainMethod(sourceOutlook,sourceMicrosoftOutlook)
