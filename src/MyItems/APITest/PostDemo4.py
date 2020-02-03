import os,requests

def PostDemo():
    URL = 'http://suggest.taobao.com/sug?code=utf-8&q=牛仔裤&callback=cb'
    
    result = requests.post(URL) #利用post方法去请求URL地址并带上参数返回的内容
    status = result.status_code #status_code返回状态码,200为成功
    content = result.text #text用于返回请求内容为文本,content用于返回请求内容为二进制码，json()用于返回请求内容为json值

    if status == 200: #增加断言，判断状态码是否为200
        print ("状态码验证通过")
    else:
        print ("状态码验证失败")
    
    if '牛仔裤ahsgd' in content: #增加断言，判断指定关键词是否在返回内容中出现
        print ("该关键词找到了")
    else:
        print ("该关键词未在结果中找到")

    print (content)

if __name__ == '__main__':
    PostDemo()
