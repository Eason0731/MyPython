#coding=utf-8 
import os,shutil,time

def MainMethod(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames):
    Choose = input("""
=========Welcome to Backup Archive Files===========
1. Backup archive files before reinstall Widnows
2. Put back archive files after reinstall Widnows
===================================================
Press AnyKey to Exit

Please Choose:""")
    if Choose == '1':
        Backup(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames)
    elif Choose == '2':
        PutBack(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames)
    else:
        exit(0)
    
def Backup(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames):
    IsBackup = '1'
    BackupFolder = time.strftime("%Y%m%d",time.localtime()) + "_Backup"
    BackupFolder = os.path.join("D:\\",BackupFolder)
    if os.path.exists(BackupFolder):
        shutil.rmtree(BackupFolder)
        print("Old backup folder: " + BackupFolder +" has been deleted successfully!")
        print("                                ")
    os.makedirs(BackupFolder)
    print("Create backup folder: " + BackupFolder + " successfully!")
    print("===================================================")
    MyFiles(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames,BackupFolder,IsBackup)
    print("===================================================")
    ExitOrNot()
        
def MyFiles(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames,BackupFolder,IsBackup):
    print(time.strftime("Start time :%Y-%m-%d %X",time.localtime())+ "\n")
    Info = "'s archive files on this PC"
    if IsBackup == '1':
        if os.path.exists(source2Kfolder):
            My2K(source2Kfolder,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found 2K Sports" + Info)
        print("                                ")
            
        if os.path.exists(sourcePES):
            PES(sourcePES,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Pro Evolution Soccer" + Info)
        print("                                ")

        if os.path.exists(sourceTDU):
            TDU(sourceTDU,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Test Drive Unlimited" + Info)
        print("                                ")
        
        if os.path.exists(sourceTencentFiles):
            TencentFiles(sourceTencentFiles,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Tencent Files" + Info)
        print("                                ")
        
        if os.path.exists(sourceBusDriver):
            BusDriver(sourceBusDriver,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Bus Driver" + Info)
        print("                                ")
        
        if os.path.exists(sourceWeChat):
            WeChatFiles(sourceWeChat,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found WeChat Files" + Info)
        print("                                ")
        
        if os.path.exists(sourceiTunes):
            iTunes(sourceiTunes,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found iTunes" + Info)
        print("                                ")

        if os.path.exists(sourcePipConfig):
            PipConfig(sourcePipConfig,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Pip config file" + Info)
        print("                                ")

        if os.path.exists(sourceChineseParents):
            ChineseParents(sourceChineseParents,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Chinese Parents" + Info)
        print("                                ")

        if os.path.exists(sourceTennisTitans):
            TennisTitans(sourceTennisTitans,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Tennis Titans" + Info)
        print("                                ")

        if os.path.exists(sourceJeep4x4):
            Jeep4x4(sourceJeep4x4,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found Jeep 4x4" + Info)
        print("                                ")
        
        if os.path.exists(sourcePopCapGames):
            PopCapGames(sourcePopCapGames,BackupFolder,IsBackup)
        else:
            print("Won't backup -- Not found PopCapGames" + Info)
        print("                                ")
        
    else:
        i = 0
        if os.path.exists(os.path.join(BackupFolder,'2K Sports')):
            i = i + 1      
            if not os.path.exists(source2Kfolder):
                My2K(source2Kfolder,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of 2K Sports " + source2Kfolder + " had existed")
            print("                                ")
                
        if os.path.exists(os.path.join(BackupFolder,'KONAMI')):
            i = i + 1 
            if not os.path.exists(sourcePES):
                PES(sourcePES,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Pro Evolution Soccer " + sourcePES + " had existed")
            print("                                ")
                
        if os.path.exists(os.path.join(BackupFolder,'Test Drive Unlimited')):
            i = i + 1  
            if not os.path.exists(sourceTDU):
                TDU(sourceTDU,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Test Drive Unlimited " + sourceTDU + " had existed")
            print("                                ")
        
        if os.path.exists(os.path.join(BackupFolder,'Tencent Files')):
            i = i + 1   
            if not os.path.exists(sourceTencentFiles):
                TencentFiles(sourceTencentFiles,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Tencent Files " + sourceTencentFiles + " had existed")
            print("                                ")
        
        if os.path.exists(os.path.join(BackupFolder,'Bus Driver')):
            i = i + 1    
            if not os.path.exists(sourceBusDriver):
                BusDriver(sourceBusDriver,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Bus Driver " + sourceBusDriver + " had existed")
            print("                                ")
        
        if os.path.exists(os.path.join(BackupFolder,'WeChat Files')):
            i = i + 1   
            if not os.path.exists(sourceWeChat):
                WeChatFiles(sourceWeChat,BackupFolder,IsBackup)
            else:
               print("Won't put back -- Path of WeChat Files " + sourceWeChat + " had existed")
            print("                                ")
        
        if os.path.exists(os.path.join(BackupFolder,'iTunes')):
            i = i + 1   
            if not os.path.exists(sourceiTunes):
                iTunes(sourceiTunes,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of iTunes " + sourceiTunes + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'pip')):
            i = i + 1   
            if not os.path.exists(sourcePipConfig):
                PipConfig(sourcePipConfig,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Pip config file " + sourcePipConfig + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'中国式家长')):
            i = i + 1   
            if not os.path.exists(sourceChineseParents):
                ChineseParents(sourceChineseParents,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Chinese Parents " + sourceChineseParents + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'Tennis Titans')):
            i = i + 1   
            if not os.path.exists(sourceTennisTitans):
                TennisTitans(sourceTennisTitans,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Tennis Titans " + sourceTennisTitans + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'Daimler')):
            i = i + 1   
            if not os.path.exists(sourceJeep4x4):
                Jeep4x4(sourceJeep4x4,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of Jeep 4x4 " + sourceJeep4x4 + " had existed")
            print("                                ")

        if os.path.exists(os.path.join(BackupFolder,'PopCap Games')):
            i = i + 1   
            if not os.path.exists(sourcePopCapGames):
                PopCapGames(sourcePopCapGames,BackupFolder,IsBackup)
            else:
                print("Won't put back -- Path of PopCap Games " + sourcePopCapGames + " had existed")
            print("                                ")
        
        if i == 0:
            IsBackup = '1'
            print(BackupFolder + " does not contain any releated backup files, this may not a correct backup folder \n")

    DeleteBackupFolder(BackupFolder,IsBackup)
    print(time.strftime("End time :%Y-%m-%d %X",time.localtime()))

def My2K(source2Kfolder,BackupFolder,IsBackup):
    SmartHint(source2Kfolder,os.path.join(BackupFolder,"2K Sports"),'2K',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'2K Sports')
        os.makedirs(BackupFolder)  
        copyFiles(source2Kfolder,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"2K Sports"), source2Kfolder)
    GetSize(source2Kfolder,'2K',IsBackup)
      
def PES(sourcePES,BackupFolder,IsBackup):
    SmartHint(sourcePES,os.path.join(BackupFolder,"KONAMI"),'Pro Evolution Soccer',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'KONAMI')
        os.makedirs(BackupFolder)
        copyFiles(sourcePES,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"KONAMI"), sourcePES)
    GetSize(sourcePES,'Pro Evolution Soccer',IsBackup)

def TDU(sourceTDU,BackupFolder,IsBackup):
    SmartHint(sourceTDU,os.path.join(BackupFolder,"Test Drive Unlimited"),'Test Drive Unlimited',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Test Drive Unlimited')
        os.makedirs(BackupFolder)  
        copyFiles(sourceTDU,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"Test Drive Unlimited"), sourceTDU)
    GetSize(sourceTDU,'Test Drive Unlimited',IsBackup)
    
def TencentFiles(sourceTencentFiles,BackupFolder,IsBackup):
    SmartHint(sourceTencentFiles,os.path.join(BackupFolder,"Tencent Files"),'Tencent Files',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Tencent Files')
        os.makedirs(BackupFolder)
        copyFiles(sourceTencentFiles,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"Tencent Files"), sourceTencentFiles)
    GetSize(sourceTencentFiles,'Tencent Files',IsBackup)
  
def BusDriver(sourceBusDriver,BackupFolder,IsBackup):
    SmartHint(sourceBusDriver,os.path.join(BackupFolder,"Bus Driver"),'Bus Driver',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Bus Driver')
        os.makedirs(BackupFolder)
        copyFiles(sourceBusDriver,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"Bus Driver"), sourceBusDriver)
    GetSize(sourceBusDriver,'Bus Driver',IsBackup)

def WeChatFiles(sourceWeChat,BackupFolder,IsBackup):
    SmartHint(sourceWeChat,os.path.join(BackupFolder,"WeChat Files"),'WeChat Files',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'WeChat Files')
        os.makedirs(BackupFolder)
        copyFiles(sourceWeChat,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"WeChat Files"), sourceWeChat)
    GetSize(sourceWeChat,'WeChat Files',IsBackup)

def iTunes(sourceiTunes,BackupFolder,IsBackup):
    SmartHint(sourceiTunes,os.path.join(BackupFolder,"iTunes"),'iTunes',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'iTunes')
        os.makedirs(BackupFolder)
        copyFiles(sourceiTunes,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,"iTunes"), sourceiTunes)
    GetSize(sourceiTunes,'iTunes',IsBackup)

def PipConfig(sourcePipConfig,BackupFolder,IsBackup):
    SmartHint(sourcePipConfig,os.path.join(BackupFolder,'pip'),'Pip config file',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'pip')
        os.makedirs(BackupFolder)
        copyFiles(sourcePipConfig,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,'pip'), sourcePipConfig)
    GetSize(sourcePipConfig,'Pip config file',IsBackup)

def ChineseParents(sourceChineseParents,BackupFolder,IsBackup):
    SmartHint(sourceChineseParents,os.path.join(BackupFolder,'中国式家长'),'Chinese Parents',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'中国式家长')
        os.makedirs(BackupFolder)
        copyFiles(sourceChineseParents,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,'中国式家长'), sourceChineseParents)
    GetSize(sourceChineseParents,'Chinese Parents',IsBackup)

def TennisTitans(sourceTennisTitans,BackupFolder,IsBackup):
    SmartHint(sourceTennisTitans,os.path.join(BackupFolder,'Tennis Titans'),'Tennis Titans',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Tennis Titans')
        os.makedirs(BackupFolder)
        copyFiles(sourceTennisTitans,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,'Tennis Titans'), sourceTennisTitans)
    GetSize(sourceTennisTitans,'Tennis Titans',IsBackup)

def Jeep4x4(sourceJeep4x4,BackupFolder,IsBackup):
    SmartHint(sourceJeep4x4,os.path.join(BackupFolder,'Daimler'),'Jeep 4x4',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'Daimler')
        os.makedirs(BackupFolder)
        copyFiles(sourceJeep4x4,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,'Daimler'), sourceJeep4x4)
    GetSize(sourceJeep4x4,'Jeep 4x4',IsBackup)

def PopCapGames(sourcePopCapGames,BackupFolder,IsBackup):
    SmartHint(sourcePopCapGames,os.path.join(BackupFolder,'PopCap Games'),'PopCap Games',IsBackup)
    if IsBackup == '1':
        BackupFolder = os.path.join(BackupFolder,'PopCap Games')
        os.makedirs(BackupFolder)
        copyFiles(sourcePopCapGames,BackupFolder)
    else:
        shutil.move(os.path.join(BackupFolder,'PopCap Games'), sourcePopCapGames)
    GetSize(sourcePopCapGames,'PopCap Games',IsBackup)
        
def PutBack(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames):
    BackupFolder = SearchBackupFolder()
    print("===================================================")
    if 'Not Exists Path' in BackupFolder:
        print("BackupFolder is not exixts and won't put back!")
    else:
        print("Backup folder is : " + BackupFolder + " \n")
        IsBackup = '2'
        MyFiles(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames,BackupFolder,IsBackup)
    print("===================================================")
    ExitOrNot()

def SmartHint(Source,Target,Fun,IsBackup):
    size = 0
    if IsBackup == '1':
        for root, dirs, files in os.walk(Source):
            for names in files:
                myfiles = os.path.join(root,names)
                size += sum([os.path.getsize(myfiles)])
    else:
        for root, dirs, files in os.walk(Target):
            for names in files:
                myfiles = os.path.join(root,names)
                size += sum([os.path.getsize(myfiles)])

    if size > (1024.00*1024.00*100.00):
        if IsBackup == '1':
            print ("Backing up the large file "+ Fun + " now and please wait a moment...")
        else:
            print ("Putting back the large file "+ Fun + " now and please wait a moment...")

def DeleteBackupFolder(BackupFolder,IsBackup):
    if not os.listdir(BackupFolder):
        shutil.rmtree(BackupFolder)
        if not os.path.exists(BackupFolder):
            if IsBackup == '1':
                print ("Empty archive files backup folder " + BackupFolder + " has been deleted successfully! \n")
            else:
                print("All archive files have been put back")
                print("Backup folder " + BackupFolder + " has been deleted successfully! \n")

def SearchBackupFolder():
    k = 0
    Dir = 'D:\\'
    Name = '_Backup'
    BackupFolder = 'Not Exists Path'
    for root,dirs,filenames in os.walk(Dir):
        for myFolder in dirs:
            if Name.lower() in myFolder.lower():
                k = k + 1
                BackupFolder = os.path.join(root,myFolder)

    return BackupFolder

def ExitOrNot():
    while(True):
        cc = input("Back to main menu? (Y/N)")
        if cc.lower() == 'y':
            MainMethod(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames)
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

def GetSize(Source,Fun,IsBackup):
    size = 0
    for root, dirs, files in os.walk(Source):
        for names in files:
            myfiles = os.path.join(root,names)
            size += sum([os.path.getsize(myfiles)])
      
    if size > (1024.00*1024.00*1024.00*1024.00):
        if IsBackup == '1':
            print("Backup " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00/1024.00/1024.00), "TB")
        else:
            print("Put back " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00/1024.00/1024.00), "TB")
    elif size > (1024.00*1024.00*1024.00):
        if IsBackup == '1':
            print("Backup " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00/1024.00), "GB")
        else:
            print("Put back " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00/1024.00), "GB")
    elif size > (1024.00*1024.00):
        if IsBackup == '1':
            print("Backup " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00), "MB")
        else:
            print("Put back " + Fun + " successfully! --- %.2f" % (size/1024.00/1024.00), "MB")
    elif size > (1024.00):
        if IsBackup == '1':
            print("Backup " + Fun + " successfully! --- %.2f" % (size/1024.00), "KB")
        else:
            print("Put back " + Fun + " successfully! --- %.2f" % (size/1024.00), "KB")
    else:
        if IsBackup == '1':
            print("Backup " + Fun + " successfully! --- %.2f" % (size), "B")
        else:
            print("Put back " + Fun + " successfully! --- %.2f" % (size), "B")

if __name__ == "__main__":
    source2Kfolder = os.path.join(os.environ['AppData'],'2K Sports') 
    sourcePES = os.path.join(os.environ['USERPROFILE'],'Documents','KONAMI')
    sourceTDU = os.path.join(os.environ['USERPROFILE'],'Documents','Test Drive Unlimited')
    sourceTencentFiles = os.path.join(os.environ['USERPROFILE'],'Documents','Tencent Files')
    sourceBusDriver = os.path.join(os.environ['USERPROFILE'],'Documents','Bus Driver')
    sourceWeChat = os.path.join(os.environ['USERPROFILE'],'Documents','WeChat Files')
    sourceiTunes = os.path.join(os.environ['USERPROFILE'],'Music','iTunes')
    sourcePipConfig = os.path.join(os.environ['USERPROFILE'],'pip')
    sourceChineseParents = os.path.join(os.environ['UserProfile'],'AppData','LocalLow','moyuwan','中国式家长')
    sourceTennisTitans = os.path.join(os.environ['AppData'],'Macromedia','Director MX 2004','Tennis Titans')
    sourceJeep4x4 = os.path.join(os.environ['AppData'],'Daimler')
    sourcePopCapGames = os.path.join(os.environ['ProgramData'],'PopCap Games')
    
    MainMethod(source2Kfolder,sourcePES,sourceTDU,sourceTencentFiles,sourceBusDriver,sourceWeChat,sourceiTunes,sourcePipConfig,sourceChineseParents,sourceTennisTitans,sourceJeep4x4,sourcePopCapGames)
