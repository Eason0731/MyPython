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
    for Package in List:
        InstallList = os.popen('pip list')
        UpdateList = os.popen('pip list --outdate')
        if Package not in InstallList.read():
            os.system('pip install ' + Package)
        else:
            print (Package + ' has installed')
        print ("                       ")
        if Package in UpdateList.read():
            os.system('pip install '+ Package + ' -U')
        else:
            print ('No need to update ' + Package)
        print ("==========================================================")
    print(time.strftime("End time :%Y-%m-%d %X",time.localtime()))
    print ("==========================================================")
    print ("                                                          ")
    print (os.popen('pip list').read())
    print ("==========================================================")
    if '' in os.popen('pip list --outdate').read():
        print ("All of the installed packages are the latest version!")
    else:
        print (os.popen('pip list --outdate').read())
    print ("==========================================================")

if __name__ == '__main__':
    PipInstall()
