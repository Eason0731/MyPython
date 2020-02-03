import os
baseurl = 'http://suggest.taobao.com'

URL_get= baseurl +'/sug?code=utf-8&q=牛仔裤&callback=cb' #用于Get获取方法调用的网址
URL_post= {'请求URL':baseurl +'/sug','Params':{'code':'utf-8','q':'牛仔裤','callback':'cb'}} #用于Post请求方法调用的网址,对应get的URL网址中的三个参数:code=utf-8&q=牛仔裤&callback=cb,用字典值编写
