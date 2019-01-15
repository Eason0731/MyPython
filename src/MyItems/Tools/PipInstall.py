import os

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
    
    for i in List:
        InstallList = os.popen('pip list')
        UpdateList = os.popen('pip list --outdate')
        if i not in InstallList.read():
            os.system('pip install ' + i)
        else:
            print (i + ' has installed')
        print ("                       ")
        if i in UpdateList.read():
            os.system('pip install '+ i + ' -U')
        else:
            print ('No need to update ' + i)
        print ("=======================")
    
    


if __name__ == '__main__':
    PipInstall()
