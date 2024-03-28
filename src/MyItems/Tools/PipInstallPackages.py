import os,time,sys

def PipInstall():
    Pillow = 'Pillow'
    backports_zoneinfo = ''
    Selenium = 'selenium'
    
    if '32 bit'in sys.version:
        Pillow = 'Pillow==9.5.0'
        Selenium = 'selenium==4.10.0'
        
    PackagesList = [
    'asgiref'
    ,'async-generator'
    ,'attrs'
    ,'certifi'
    ,'cffi'
    ,'chardet'
    ,'charset-normalizer'
    ,'colorama'
    ,'cryptography'
    ,'ddt'
    ,'Django'
    ,'exceptiongroup'
    ,'h11'
    ,'idna'
    ,'iniconfig'
    ,'Naked'
    ,'numpy'
    ,'outcome'
    ,'packaging'
    ,Pillow
    ,'pip'
    ,'pluggy'
    ,'progressbar'
    ,'psutil'
    ,'pycparser'
    ,'pycryptodome'
    ,'Pygments'
    ,'pyOpenSSL'
    ,'pypiwin32'
    ,'Pypubsub'
    ,'PySocks'
    ,'pytest'
    ,'pytz'
    ,'pywin32'
    ,'PyYAML'
    ,'rarfile'
    ,'requests'
    ,'robotframework'
    ,'robotframework-pythonlibcore'
    ,'robotframework-ride'
    ,'robotframework-selenium2library'
    ,'robotframework-seleniumlibrary'
    ,Selenium
    ,'setuptools'
    ,'shellescape'
    ,'six'
    ,'sniffio'
    ,'sortedcontainers'
    ,'sqlparse'
    ,'tomli'
    ,'trio'
    ,'trio-websocket'
    ,'typing_extensions'
    ,'tzdata'
    ,'unrar'
    ,'urllib3'
    ,'WMI'
    ,'wsproto'
    ,'wxPython']
    
    if sys.version_info < (3,10):
        backports_zoneinfo = 'backports.zoneinfo'
        PackagesList.append(backports_zoneinfo)
    
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
            if 'already satisfied' in os.popen('pip install ' + myPackage).read():
                print (myPackage + ' has installed')
                Installed = Installed + 1
                InstalledList.append(myPackage)
            else:
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
    print ("                                                          ")
    if '32 bit'in sys.version:
        print (os.popen('pip list --outdated | findstr /v /r "Pillow selenium"').read()) #findstr /v /r 可以忽略多个第三方的库的包,eg:pip list --outdated | findstr /v /r "numpy pandas scipy",如只需忽略一个包可以用该指令,eg:pip list --outdated | findstr /v Pillow
    else:
        print (os.popen('pip list --outdate').read())
    print ("==========================================================")
    print ("Start time :" + StartTime)
    print (time.strftime("End time :%Y-%m-%d %X",time.localtime()))
    print ("==========================================================")

if __name__ == '__main__':
    PipInstall()
