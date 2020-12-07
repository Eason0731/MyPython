f = open("guests.txt",'w')

for i in range(1,3001):
    realname = "Eason" + str(i)
    phone = 1380011000 + i
    email = "eason"+str(i)+"@qq.com"
    create_time = "datetime('now')"

    sql_insert = 'insert into sign_guest(realname,phone,email,sign,create_time,event_id) VALUES ("'+realname+'",'+str(phone)+ ',"'+email+'",0,'+create_time+',1);'
    f.write(sql_insert)
    f.write("\n")

f.close()
    
    
