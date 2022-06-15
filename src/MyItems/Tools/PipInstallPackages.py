import os,time

def PipInstall():
    PackagesList = [
    'asgiref'
    ,'async-generator'
    ,'attrs'
    ,'backports.zonein'
    ,'certifi'
    ,'cffi'
    ,'chardet'
    ,'charset-normalizer'
    ,'cryptography'
    ,'ddt'
    ,'Django'
    ,'h11'
    ,'idna'
    ,'Naked'
    ,'numpy'
    ,'outcome'
    ,'Pillow'
    ,'pip'
    ,'progressbar'
    ,'pycparser'
    ,'pycryptodome'
    ,'pyOpenSSL'
    ,'pypiwin32'
    ,'PySocks'
    ,'pytz'
    ,'pywin32'
    ,'PyYAML'
    ,'rarfile'
    ,'requests'
    ,'robotframework'
    ,'selenium'
    ,'setuptools'
    ,'shellescape'
    ,'six'
    ,'sniffio'
    ,'sortedcontainers'
    ,'sqlparse'
    ,'trio'
    ,'trio-websocket'
    ,'tzdata'
    ,'unrar'
    ,'urllib3'
    ,'WMI'
    ,'wsproto']
    
    print ("==========================================================")
    StartTime = (time.strftime("%Y-%m-%d %X",time.localtime()))
    Install = 0
    InstallList = []

    Installed = 0
    InstalledList = []

    NoUpdated = 0
    NoUpdatedList = []

    Updated = 0
    UpdatedList = []

    for myPackage in PackagesList:
        InstallPackagesList = os.popen('pip list')
        UpdatePackagesList = os.popen('pip list --outdate')
        if myPackage not in InstallPackagesList.read():
            os.system('pip install ' + myPackage)
            Install = Install + 1
            InstallList.append(myPackage)
        else:
            print (myPackage + ' has installed')
            Installed = Installed + 1
            InstalledList.append(myPackage)
        print ("                       ")
        if myPackage in UpdatePackagesList.read():
            os.system('pip install '+ myPackage + ' -U')
            Updated = Updated + 1
            UpdatedList.append(myPackage)
        else:
            print ('No need to update ' + myPackage)
            NoUpdated = NoUpdated + 1
            NoUpdatedList.append(myPackage)

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
        print ("{0} ({1}) ".format(str(Install),','.join(InstallList)) + pkg +" insalled successfully on this PC!")
    print ("                                                          ")  
    print (os.popen('pip list').read())
    print ("==========================================================")
    if Updated == 0:
        if NoUpdated == 1:
            pkg = 'package was'
        else:
            pkg = 'packages were'
        print ("{0} ({1}) ".format(str(NoUpdated),','.join(NoUpdatedList)) + pkg + " installed on this PC are the latest version!")
    else:
        if Updated == 1:
            pkg = 'package has'
        else:
            pkg = 'packages have'
        print ("{0} ({1}) ".format(str(Updated),','.join(UpdatedList)) + pkg + " updated successfully on this PC!")
    print (os.popen('pip list --outdate').read())
    print ("==========================================================")
    print ("Start time :" + StartTime)
    print (time.strftime("End time :%Y-%m-%d %X",time.localtime()))
    print ("==========================================================")

if __name__ == '__main__':
    PipInstall()
