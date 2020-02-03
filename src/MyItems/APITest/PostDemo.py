import os,requests

def PostDemo():
    URL = 'http://suggest.taobao.com/sug'
    Params = {'code':'utf-8','q':'牛仔裤','callback':'cb'}
    #对应URL网址中的三个参数:code=utf-8&q=牛仔裤&callback=cb
    
    result = requests.post(URL,Params) #利用post方法去请求URL地址并带上参数返回的内容
    status = result.status_code #status_code返回状态码,200为成功
    content = result.content #text用于返回请求内容为文本,content用于返回请求内容为二进制码，json()用于返回请求内容为json值

    print (status)
    print (content)

if __name__ == '__main__':
    PostDemo()
