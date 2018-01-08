# -*- coding: utf-8 -*-
import os
import re
import shutil
import time
import sys
import ViewPCInfos

def MainFunction():
    Choose = input ("""
=============Welcome to File Operation=============
1. Replace content on txt files
2. Delete file or folder
3. Batch delete file or folder
4. Copy file or folder
5. Move file or folder
6. Find contents on txt files
7. Find files or folder on folder
8. Rename file or folder
9. Batch Rename file or folder
10. Calculate the file or folder size
11. Decompress rar and zip file
12. Compress file or folder to zip
13. Open file or folder
14. View PC infos


=========  """+ GetDate() +"""  =========

Press AnyKey to Exit
        
Please choose : """)
    Fun = sys._getframe().f_code.co_name
    if Choose == '1':
        print("===========Replace content on txt files============")
        Dir = input ("Please input folder path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                ReplaceOnTxt(Dir)
            else:
                ExistOrNot(Dir)
                                  
    elif Choose == '2':
        print("===============Delete file or folder===============")
        Dir = input ("Please input folder or file path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                Delete(Dir)
            else:
                ExistOrNot(Dir)

    elif Choose == '3':
        print("===========Batch Delete files or folder ==========")
        Dir  = input ("Please input folder path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                BatchAndFindOnDirs(Dir,'Del')
            else:
                ExistOrNot(Dir)

    elif Choose == '4':
        print("===============Copy file or folder=================")
        Source = input ("Please input folder or file path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                Copy(Source)
            else:
                ExistOrNot(Source)
            
    elif Choose == '5':
        print("===============Move file or folder=================")
        Source = input ("Please input source folder or file path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                Move(Source)
            else:
                ExistOrNot(Source)
                    
    elif Choose == '6':
        print("=============Find contents on txt files============")
        Dir  = input ("Please input folder path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                FindOnTxt(Dir)
            else:
                ExistOrNot(Dir)
                
    elif Choose == '7':
        print("===========Find files or folder on folder==========")
        Dir  = input ("Please input folder path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                BatchAndFindOnDirs(Dir,'Find')
            else:
                ExistOrNot(Dir)

    elif Choose == '8':
        print("===============Rename file or folder===============")  
        Source = input ("Please input folder or file path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                Rename(Source)
            else:
                ExistOrNot(Source)

    elif Choose == '9':
        print("============Batch Rename files or folder==========")
        Dir = input ("Please input folder or file path: ")
        if os.path.exists(Dir):
            FormatJudge(Dir,Fun)
            BatchAndFindOnDirs(Dir,'Rename')
        elif not Dir.strip():
            EmptyOrNot(Fun)
        else:
            ExistOrNot(Dir)
            
    elif Choose == '10':
        print("========Calculate the file or folder size==========")  
        Source = input ("Please input folder or file path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                GetSize(Source)
            else:
                ExistOrNot(Source)

    elif Choose == '11':
        print("==========Decompress rar and zip file=============")  
        Source = input("Please input compressed file path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                Decompress(Source)
            else:
                ExistOrNot(Source)

    elif Choose == '12':
        print("=========Compress file or folder to zip===========")  
        Source = input("Please input file or folder path: ")
        if not Source.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Source):
                FormatJudge(Source,Fun)
                CompressZip(Source)
            else:
                ExistOrNot(Source)
    
    elif Choose == '13':
        print("===============Open file or folder=================")
        Dir = input ("Please input file or folder path: ")
        if not Dir.strip():
            EmptyOrNot(Fun)
        else:
            if os.path.exists(Dir):
                FormatJudge(Dir,Fun)
                OpenFileOrFolder(Dir)
            else:
                ExistOrNot(Dir)
    
    elif Choose == '14':
        ViewPCInfos.ViewPCInfos()

    else:
        exit(1)
      
def ReplaceOnTxt(Dir):
    if os.path.isdir(Dir):
        k = 0
        c = 0
        while 1:
            Original = input("Please input what to find: ")
            if not Original.strip():
                 print("Cannot input empty search content, please input again!")
            else:
                break
        while 1:
            Replace = input("Please input what to replace: ")
            if not Replace.strip():
                 print("Cannot input empty replace content, please input again!")
            else:
                break
        print("=================== Start =========================")
        print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
        for root,dirs,filenames in os.walk(Dir):
            for myFile in filenames:
                if 'txt' in myFile:
                    k+=1
                    TxtFile = os.path.join(root,myFile)
                    files = open (TxtFile,'r') 
                    content = files.read()
                    files.close()
                    Original = Original.lower()
                    content = content.lower()
                    if Original in content:
                        c+=1         
                        files = open (TxtFile,'w') 
                        files.writelines(content.replace (Original, Replace))
                        files.close()
                        print(Original + " has been replaced as " + Replace + " on file "+ TxtFile +" successfully!")
                        print("   ")
                    files.close()
                    
        if c == 0 and k != 0:
            print(Original + " didn't found on " + Dir)       
                
        if k == 0:
            print("There is no txt files under folder " + Dir)

        print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
        print("=================== Finish ========================")
    else:
        print(Dir + " is a file path , please input a folder path")
    CountineOrExit()

def Delete(Dir):
    while 1:
        IsDel = input("Are you sure to delete " + Dir +"? (Y/N)")
        if IsDel.lower() == 'y':
            break
        elif IsDel.lower() == 'n':
            CountineOrExit()
            break
    
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if os.path.isfile(Dir):
        os.remove(Dir)
    elif os.path.isdir(Dir):
        shutil.rmtree(Dir)  
    if not os.path.exists(Dir):
        print(Dir + " has been deleted successfully!")
    else:
        print(Dir + " has been deleted failed!")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def BatchAndFindOnDirs(Dir,Fun):
    k = 0
    if os.path.isdir(Dir):
        while 1:
            Find = input ("What want to find on this folder? ")
            if not Find.strip():
                print("Cannot input empty file or folder name, please input again!")
            else:
                break
            
        if 'Rename' in Fun:
            while 1:
                Replace = input("Please input new name to replace: ")
                if not Replace.strip():
                    print("Cannot input empty replace content, please input again!")
                else:
                    break

        if 'Del' in Fun:
            while 1:
                IsDel = input("Are you sure to batch delete files or folders? (Y/N)")
                if IsDel.lower() == 'y':
                    break
                elif IsDel.lower() == 'n':
                    CountineOrExit()
                    break
        
        print("=================== Start =========================")
        print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
        for root,dirs,filenames in os.walk(Dir):
            FTypes = [filenames,dirs]
            for FD in FTypes:
                for myFile in FD:
                    if Find.lower() in myFile.lower():
                        k = k + 1
                        F = os.path.join(root,myFile)
                        if 'Del' in Fun:
                            if os.path.isfile(F):
                                os.remove(F)
                            elif os.path.isdir(F):
                                shutil.rmtree(F)
                            if not os.path.exists(F):
                                print(F + " has been deleted successfully!")
                                print("  ")
                            else:
                                print(F + " has been deleted failed!")
                        
                        elif 'Find' in Fun:
                            print(Find + " has found on " + F)
                            print("  ")
                        elif 'Rename' in Fun:
                            Find = Find.lower()
                            myFile = myFile.lower()
                            OldName = os.path.join(root,myFile)
                            myFile = myFile.replace(Find,Replace)
                            NewName = os.path.join(root,myFile)
                            os.rename (OldName,NewName)
                            if os.path.exists(NewName):
                                print(OldName +" has been replaced as " + NewName + " successfully!")
                                print("   ")
            
        if k == 0:
            print(Find + " didn't found on " + Dir)
        print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
        print("=================== Finish ========================")
    else:
        print(Dir + " is a file path , please input a folder path")
    CountineOrExit()

def Copy(Source):
    Fun = sys._getframe().f_code.co_name
    while 1:
        Target = input ("Please input target folder path: ")
        if not Target.strip():
            EmptyOrNot(Fun)
        elif not '\\' in Target:
            FormatJudge(Target,Fun)
        elif os.path.isfile(Target):
            print("Cannot copy to file path " + Target + " please input again!")
        else:
            break
    TargetFolderEmptyOrNot(Source,Target,Fun)
    Disk = '\\'.join(Target.split("\\")[:1])
    if os.path.exists(Disk):
        if not os.path.exists(Target):
            os.makedirs(Target)
    else:
        print(Disk + " is not exists on this PC, cannot copy")
        CountineOrExit()
    Type = Source.split("\\")[-1]
    Target = os.path.join(Target,Type)
    if os.path.exists(Target):
        if Source.lower() == Target.lower():    
            print("Cannot copy same file or folder to origin path")
            CountineOrExit()
        else:
            OverwriteOrNot(Source,Target)
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if os.path.isdir(Source):
        if not os.listdir(Source):
            shutil.copytree(Source,Target)
        else:
            copyFiles(Source,Target)
    elif os.path.isfile(Source):
        shutil.copy (Source,Target)
    print(Source + " has copied to " + '\\'.join(Target.split("\\")[:-1]) + " successfully!")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

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

def Move(Source):
    Fun = sys._getframe().f_code.co_name
    while 1:
        Target = input ("Please input target folder path: ")
        if not Target.strip():
            EmptyOrNot(Fun)
        elif not '\\' in Target:
            FormatJudge(Target,Fun)
        elif os.path.isfile(Target):
            print("Cannot move to file path " + Target + " please input again!")
        else:
            break
    TargetFolderEmptyOrNot(Source,Target,Fun)
    Disk = '\\'.join(Target.split("\\")[:1])
    Type = Source.split("\\")[-1]
    if os.path.exists(Disk):
        if not os.path.exists(Target):
            os.makedirs(Target)
    else:
        print(Disk + " is not exists on this PC, cannot move")
        CountineOrExit()
    Target = os.path.join(Target,Type)
    if os.path.exists(Target):
        if Source.lower() == Target.lower():
            print("Cannot move file or folder to origin path")
            CountineOrExit()
        else:
            OverwriteOrNot(Source,Target)
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if os.path.isfile(Source):
        if os.path.exists(Target):
            os.remove(Target)
        shutil.move (Source,Target)
    elif os.path.isdir(Source):
        if not os.listdir(Source):
            shutil.copytree(Source,Target)
        else:
            copyFiles(Source,Target)                    
        shutil.rmtree(Source)
    if os.path.exists(Target):
        print(Source + " has been moved from " + "\\".join(Source.split("\\")[0:-1]) + " to " + "\\".join(Target.split("\\")[0:-1]) + " successfully!")
    else:
        print(Source + " has been moved failed!")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def FindOnTxt(Dir):
    if os.path.isdir(Dir):
        c = 0
        k = 0
        while 1:
            Content = input ("What want to find on txt file? ")
            if not Content.strip():
                print("Cannot input empty search content, please input again!")
            else:
                break
        print("=================== Start =========================")
        print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
        for root,dirs,filenames in os.walk(Dir):         
            for myFile in filenames:
                if 'txt' in myFile:
                    k+=1
                    i = 0
                    TxtFile = os.path.join(root,myFile)
                    f = open (TxtFile, 'r')
                    Filecontent = f.readlines()              
                    for eachline in Filecontent:
                        if Content.lower() in eachline.lower():
                            i+=1
                            c+=1
                    f.close()
                    if i > 0:
                        print(Content + " found on " + TxtFile + " for " + str(i) + " times")

        if c == 0 and k != 0:
            print(Content + " didn't found on " + Dir)
            
        if k == 0:
            print("There is no txt files under folder " + Dir)

        print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
        print("=================== Finish ========================")
    else:
        print(Dir + " is a file path , please input a folder path")   
    CountineOrExit()
            
def Rename(Source):
    while 1:
        Target = input ("Please input new name want to replace: ")
        if not Target.strip():
            print("Cannot input empty replace content, please input again!")
        else:
            break
    Source = os.path.abspath(Source)
    Target = os.path.join(os.path.split(Source)[0],Target)
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if os.path.exists(Target):
        print(Source + " has already exists, cannot be renamed!")
    else:
        os.rename (Source,Target)
        print(Source + " has been renamed as " + Target +" successfully!")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()
            

def GetSize(Source):
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    size = 0
    if os.path.isfile(Source):
        size = os.path.getsize(Source)
    elif os.path.isdir(Source):
        for root, dirs, files in os.walk(Source):
            for names in files:
                myfiles = os.path.join(root,names)
                size += sum([os.path.getsize(myfiles)])
    print("The size of " + Source + " are %.2f" % (size/1024.00/1024.00), "MB")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def Decompress(Source):
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    UnzipPath = "".join(Source.split('.')[:-1])
    if 'zip' in Source:
        import zipfile
        ZFile = zipfile.ZipFile(Source)
        if os.path.exists(UnzipPath):
            print(UnzipPath + " is exists and won't cover!")
        else:
            os.mkdir(UnzipPath)
            for names in ZFile.namelist():
                ZFile.extract(names,UnzipPath)
            print(Source + " has been decompressed to " + UnzipPath + " successfullly!")
            ZFile.close()
    elif 'rar' in Source:
        Output = os.popen('pip list')
        if 'rarfile' not in Output.read():
            os.system('pip install rarfile')
            os.system('pip install unrar')
        import rarfile
        rar = rarfile.RarFile(Source)
        if os.path.exists(UnzipPath):
            print(UnzipPath + " is exists and won't cover!")
        else:
            os.mkdir(UnzipPath)
            rar.extractall(UnzipPath)
            print(Source + " has been decompressed to " + UnzipPath + " successfullly!")
            rar.close()  
    else:
        print("Cannot decompress " + Source + " as its not the correct format")    
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def CompressZip(Source):
    import zipfile
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    if os.path.isdir(Source):
        ZFile = "\\".join(Source.split('\\'))+".zip"
        types = 'dir'
    elif os.path.isfile(Source):
        ZFile = os.path.splitext(Source)[0]+'.zip'
        types = 'file'
    if 'file' in types:
        if os.path.exists(ZFile):
            print(ZFile + " is exists and won't cover!")
        else:
            Zip_File = zipfile.ZipFile(ZFile,'w',zipfile.ZIP_DEFLATED,allowZip64=True)
            os.chdir(os.path.dirname(Source)) 
            Myfile = "".join(Source.split('\\')[-1])
            Zip_File.write(Myfile)
            print(Source + " has been compressed as " + ZFile + " succeessfully!")
            Zip_File.close()
    if 'dir' in types:
        if os.path.exists(ZFile):
            print(ZFile + " is exists and won't cover!")
        else:
            Zip_File = zipfile.ZipFile(ZFile,'w',zipfile.ZIP_DEFLATED,allowZip64=True)
            for dirpath, dirnames, filenames in os.walk(Source):  
                for filename in filenames:  
                    Zip_File.write(os.path.join(dirpath,filename))
            print(Source + " has been compressed as " + ZFile + " succeessfully!")
            Zip_File.close()
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def OpenFileOrFolder(Dir):
    print("=================== Start =========================")
    print(time.strftime("Start Time :%Y-%m-%d %X",time.localtime()))
    os.startfile(Dir)
    print(Dir + " has been opened sucessfully!")
    print(time.strftime("End Time :%Y-%m-%d %X",time.localtime()))
    print("=================== Finish ========================")
    CountineOrExit()

def CountineOrExit():
    print("===================================================")
    IsExit = input ("Countine(Y) or Exit(N)? ")
    while(1):
        if IsExit.upper() == 'Y':
            MainFunction()
        elif IsExit.upper() == 'N':
            print("Bye~")
            exit(0)
        else:
            print("You have inputed illegal character,try again!")
            CountineOrExit()
            break
            
def EmptyOrNot(Fun):
    print("===================================================")
    print("Please do not input empty infos")
    if 'Main' in Fun:
        CountineOrExit()
    else:
        print("===================================================")
        

def ExistOrNot(Dir):
    print("===================================================")
    print("{0} is NOT Exist!" .format(Dir))
    CountineOrExit()
    
def OverwriteOrNot(Source,Target):
    while(1):
        if os.path.isfile(Target):
            IsConver = input ("There is a same file on target file , would you still want to operate it? (Y/N) ")
        elif os.path.isdir(Target):
            IsConver = input ("There is a same folder on target folder , would you still want to operate it? (Y/N) ")              
        if IsConver.lower() == 'y':
            if os.path.isdir(Target):
                if not os.listdir(Source) and not os.listdir(Target):
                    shutil.rmtree(Target) 
            break
        elif IsConver.lower() == 'n':
            CountineOrExit()
        
def FormatJudge(Dir,Fun):
    if not '\\' in Dir:
        print("===================================================")
        print("The format of " + Dir + " is incorrect! Should with '\\'")
        if 'Main' in Fun:
            CountineOrExit()
        else:
            print("===================================================")

def TargetFolderEmptyOrNot(Source,Target,Fun):
     if not Target.strip():
         print("===================================================")
         print("Do not input the empty infos. Please input again!")
         if 'Copy' in Fun:
             Copy(Source)
         elif 'Move' in Fun:
             Move(Source)
             
def GetDate():
    Date = time.strftime("%Y-%m-%d , %A", time.localtime())
    return "Today is " + Date

if __name__== '__main__':
    MainFunction()
