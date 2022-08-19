import smtplib,os,time,unittest
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
#发送邮件需要用到的库

def Via_QQ(Latest_Report_Path): #发送邮件方法
    #-----------1.跟发件相关的参数------
    smtpserver = 'smtp.qq.com' #发件服务器
    port = 465 #端口
    username = 'lonlon29@qq.com' #发件箱用户名
    #password = 'uvwugrwppapdcahd' #旧的授权码
    password = 'wqcvkpqqhmbjcaaf'#发件箱密码
    sender = 'lonlon29@qq.com' #发件人邮箱
    receiver = ['lonlon29@sina.cn','Eason.Zhang0731@outlook.com'] #收件人邮箱
    mailname = 'qq'
    Send_Mail(smtpserver,port,username,password,sender,receiver,mailname,Latest_Report_Path)
    """
    # ----------2.编辑邮件的内容------
    #读文件
    f = open(Latest_Report_Path, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化回归测试报告", 'utf-8').encode()#主题
    #msg['From'] = Header(u'测试人员 <%s>'%sender) #发件人
    msg['From'] = Header(sender) #发件人

    #msg['To'] = Header(u'测试负责人 <%s>'%receiver) #收件人
    msg['To'] = Header(u'<%s>'%receiver) #收件人
    msg['To'] = ';'.join(receiver)
    
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="Test_Report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver) # 连服务器
        #smtp.login(sender, password)
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password) # 登录
        smtp.sendmail(sender, receiver, msg.as_string()) # 发送
        smtp.quit()

    ##发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com') # 邮箱服务器
    smtp.login(username, password) # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送者和接收者
    smtp.quit()
    print("邮件已通过QQ邮箱发出！注意查收。")
    """

def Via_Sina(Latest_Report_Path): #发送邮件方法
    #-----------1.跟发件相关的参数------
    smtpserver = 'smtp.sina.cn' #发件服务器
    port = 25 #端口
    username = 'lonlon29@sina.cn' #发件箱用户名
    #password = '2e059d17a6db438f' #旧的授权码
    password = 'e7be22189ff09318'#发件箱密码
    sender = 'lonlon29@sina.cn' #发件人邮箱
    receiver = ['lonlon29@qq.com','Eason.Zhang0731@outlook.com'] #收件人邮箱
    mailname = 'sina'
    Send_Mail(smtpserver,port,username,password,sender,receiver,mailname,Latest_Report_Path)
    """
    # ----------2.编辑邮件的内容------
    #读文件
    f = open(Latest_Report_Path, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header("自动化回归测试报告", 'utf-8').encode()#主题
    msg['From'] = Header(sender) #发件人，新浪邮箱的发件人必须与之前sender中的邮箱一致，不能添加其他信息，否则会有不匹配报错返回
    #msg['To'] = Header(u'测试负责人 <%s>'%receiver) #收件人
    msg['To'] = Header(u'<%s>'%receiver) #收件人
    msg['To'] = ';'.join(receiver) #';'
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="Test_Report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver) # 连服务器
        #smtp.login(sender, password)
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password) # 登录
        smtp.sendmail(sender, receiver, msg.as_string()) # 发送
        smtp.quit()

    ##发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.sina.com') # 邮箱服务器
    smtp.login(username, password) # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送者和接收者
    smtp.quit()
    print("邮件已通过新浪邮箱发出！注意查收。")
    """    

def Send_Mail(smtpserver,port,username,password,sender,receiver,mailname,Latest_Report_Path):
    # ----------2.编辑邮件的内容------
    Current_Time = time.strftime("%Y-%m-%d %H:%M:%S")
    #读文件
    f = open(Latest_Report_Path, 'rb')
    mail_body = f.read()
    f.close()
    # 邮件正文是MIMEText
    body = MIMEText(mail_body, 'html', 'utf-8')
    # 邮件对象
    msg = MIMEMultipart()
    msg['Subject'] = Header(Current_Time + "执行的自动化回归测试已完成,请查收报告！", 'utf-8').encode() #主题

    msg['From'] = Header(sender) #发件人

    #msg['To'] = Header(u'测试负责人 <%s>'%receiver) #收件人
    msg['To'] = Header(u'<%s>'%receiver) #收件人
    msg['To'] = ';'.join(receiver)
    
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="Test_Report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver) # 连服务器
        smtp.login(sender, password)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, password) # 登录
        smtp.sendmail(sender, receiver, msg.as_string()) # 发送
        smtp.quit()

    ##发送邮件
    smtp = smtplib.SMTP()
    
    if mailname == 'qq':
        smtp.connect('smtp.qq.com') # 邮箱服务器
    elif mailname == 'sina':
        smtp.connect('smtp.sina.cn')
        
    smtp.login(username, password) # 登录邮箱
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送者和接收者
    smtp.quit()

    if mailname == 'qq':
        print("邮件已通过QQ邮箱发出！注意查收。")
    elif mailname == 'sina':
        print("邮件已通过新浪邮箱发出！注意查收。")
        
