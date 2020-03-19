import os,time,shutil

def KnivesOutDatas():
    Choose = input ("""
==========================
1. Backup game datas of Knives Out
2. Put back game datas of Knives Out

Press AnyKey to Exit
        
Please choose : """)

    if Choose == '1':
        Code = 1
    elif Choose == '2':
        Code = 2
    else:
        exit(1)
    
    BackupOrPutBack(Code)
    CountineOrExit()

def BackupOrPutBack(Code):
    GamePath_1 = os.path.join('C:\\','Program Files (x86)','hyxd','LocalData')
    GamePath_2 = os.path.join('C:\\','Program Files','hyxd','LocalData')
    BackupFoloder = os.path.join('D:\\','Knives_Out_Datas_Backup','LocalData')
        
    if os.path.exists(GamePath_1):
        GamePath = GamePath_1
        print (GamePath + " was found!")
    elif os.path.exists(GamePath_2):
        GamePath = GamePath_2
        print (GamePath + " was found!")
    else:
        print ("You didn't install game on PC, please install it")
        CountineOrExit()
    print("===================================================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if Code == 1:
        if os.path.exists(os.path.join('D:\\','Knives_Out_Datas_Backup')):
            shutil.rmtree(os.path.join('D:\\','Knives_Out_Datas_Backup'))
            
        GetSize(GamePath)
        print ("Backing up now..........") 
        shutil.copytree(GamePath,BackupFoloder)
        if os.path.exists(BackupFoloder):
            print ("Backup game datas successfully!")
    
    elif Code == 2:
        if not os.path.exists(os.path.join('D:\\','Knives_Out_Datas_Backup')):
            print ("Not found backup game datas folder,please backup it")
            CountineOrExit()
            
        GetSize(BackupFoloder)
        print ("Putting back now..........")
        if os.path.exists(GamePath):
            print ("Deleting original game datas")
            shutil.rmtree(GamePath)
            
        shutil.copytree(BackupFoloder,GamePath)
        if os.path.exists(GamePath):
            print ("Put back game datas successfully!")
            shutil.rmtree(os.path.join('D:\\','Knives_Out_Datas_Backup'))
            print ("Delete backup game datas successfully!")
    print("===================================================")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
            
def GetSize(Source):
    size = 0
    if os.path.isfile(Source):
        size = os.path.getsize(Source)
    elif os.path.isdir(Source):
        for root, dirs, files in os.walk(Source):
            for names in files:
                myfiles = os.path.join(root,names)
                size += sum([os.path.getsize(myfiles)])
    if size > (1024.00*1024.00*1024.00*1024.00):
        print("The size of " + Source + " are %.2f" % (size/1024.00/1024.00/1024.00/1024.00), "TB")
    elif size > (1024.00*1024.00*1024.00):
        print("The size of " + Source + " are %.2f" % (size/1024.00/1024.00/1024.00), "GB")
    elif size > (1024.00*1024.00):
        print("The size of " + Source + " are %.2f" % (size/1024.00/1024.00), "MB")
    elif size > (1024.00):
        print("The size of " + Source + " are %.2f" % (size/1024.00), "KB")
    else:
        print("The size of " + Source + " are %.2f" % (size), "B")
    
def CountineOrExit():
    print("===================================================")
    IsExit = input ("Countine(Y) or Exit(N)? ")
    while(1):
        if IsExit.upper() == 'Y':
            KnivesOutDatas()
        elif IsExit.upper() == 'N':
            print("Bye~")
            exit(1)
        else:
            print("You have inputed illegal character,try again!")
            CountineOrExit()
            break

if __name__ == '__main__':
    KnivesOutDatas()
