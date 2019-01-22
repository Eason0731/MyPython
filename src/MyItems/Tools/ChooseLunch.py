import os
import random

def Main():
    while (1):
        People = input ("""
Choose number of people:
1 -- Single
2 -- Multi-people

""")
        if People == '1':
            ChooseLunch('S')
            break
        elif People == '2':
            ChooseLunch('M')
            break
        else:
            print ("Do not input illegal number, please input again!")

def ChooseLunch(People):
    Week = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    
    if 'S' in People:
        LunchList = ['老广东排骨年糕','盒饭','福荣祥烧腊','吉祥馄饨','原素Essence西餐','杨铭宇黄焖鸡米饭',
             '东池便当','大阪牛肉饭','福客桂林米粉','麻辣烫','文庙菜饭',
             '羊肉泡馍','壹只蟹蟹煲饭','香酥脆皮鸡米饭','广东煲仔饭','喵七公','马来一号',
             '京都牛肉盒子饭','CUTiE咖喱屋','梁小猴港式铁板炒饭','隋炀帝炒饭']
    
    if 'M' in People:
        LunchList = ['小食堂','吉祥馄饨','樱桃菜饭骨头汤','小饭店','鹅庄','麦当劳','五芳斋']  
        
    for Day in Week:
        print ("We decided "+ Day +" 's lunch is .....")
        random.shuffle(LunchList)
        Item = random.choice(LunchList)
        print (Item)
        LunchList.remove(Item)
        print ("            ")
    
    ChooseAgain()

def ChooseAgain():
    while 1:
        CC = input("Choose again or not?(Y/N) ")
        if CC.upper() == 'Y':
            Main()
            break
        elif CC.upper() == 'N':
            break
        else:
            print ("Do not input illegal character, please input again!")
            
if __name__ == '__main__':
    Main()
