import EasonURL,os,requests

def PostDemo():
    result = requests.post(EasonURL.URL_post['请求URL'],EasonURL.URL_post['Params']) #先导入的EasonURL类中的URL_post地址，再使用post方法去请求URL地址返回的内容，请求格式使用字典值
    status = result.status_code #status_code返回状态码,200为成功
    content = result.content #text用于返回请求内容为文本,content用于返回请求内容为二进制码，json()用于返回请求内容为json值

    if status == 200: #增加断言，判断状态码是否为200
        print ("状态码验证通过")
    else:
        print ("状态码验证失败")

    print (status)
    print (content) #因为展示测试的接口没有json，所以只能输出content

if __name__ == '__main__':
    PostDemo()
