import os,time

def PipInstall():
    List = ['certifi'
    ,'chardet'
    ,'ddt'
    ,'Django'
    ,'idna'
    ,'numpy'
    ,'pip'
    ,'progressbar'
    ,'pypiwin32'
    ,'pytz'
    ,'pywin32'
    ,'rarfile'
    ,'requests'
    ,'selenium'
    ,'setuptools'
    ,'urllib3'
    ,'WMI']
    print ("==========================================================")
    print(time.strftime("Start time :%Y-%m-%d %X",time.localtime()))
    Install = 0
    InstallList = []
    
    Installed = 0
    InstalledList = []
    
    Updated = 0
    UpdatedList = []
    
    for Package in List:
        InstallPackagesList = os.popen('pip list')
        UpdatePackagesList = os.popen('pip list --outdate')
        if Package not in InstallPackagesList.read():
            os.system('pip install ' + Package)
            Install = Install + 1
            InstallList.append(Package)
        else:
            print (Package + ' has installed')
            Installed = Installed + 1
            InstalledList.append(Package)
        print ("                       ")
        if Package in UpdatePackagesList.read():
            os.system('pip install '+ Package + ' -U')
            Updated = Updated + 1
            UpdatedList.append(Package)
        else:
            print ('No need to update ' + Package)
        
        print ("==========================================================")
    print(time.strftime("End time :%Y-%m-%d %X",time.localtime()))
    print ("==========================================================")
    if Install == 0:
        if Installed == 1:
            pkg = 'package was'
        else:
            pkg = 'packages were'
        print ("There are {0} ({1}) ".format(str(Installed),','.join(InstalledList)) + pkg + " insalled on this PC!")
    else:
        if Install == 1:
            pkg = 'package has'
        else:
            pkg = 'packages have'
        print ("{0} ({1}) ".format(str(Install),','.join(InstallList)) + pkg +" insalled on this PC successfully!")
    print ("                                                          ")  
    print (os.popen('pip list').read())
    print ("==========================================================")
    if Updated == 0:
        if Installed == 1:
            pkg = 'package was'
        else:
            pkg = 'packages were'
        print ("{0} ({1}) ".format(str(Installed),','.join(InstalledList)) + pkg + " installed on this PC are the latest version!")
    else:
        if Updated == 1:
            pkg = 'package has'
        else:
            pkg = 'packages have'
        print ("{0} ({1}) ".format(str(Updated),','.join(UpdatedList)) + pkg + " updated on this PC successfully!")
    print (os.popen('pip list --outdate').read())
    print ("==========================================================")

if __name__ == '__main__':
    PipInstall()
