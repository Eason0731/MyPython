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
    LunchList = ['老广东','福荣祥烧腊','吉祥馄饨','原素Essence西餐','杨铭宇黄焖鸡米饭',
             '东池便当','大阪牛肉饭','福客桂林米粉','杨国富麻辣烫','文庙菜饭',
             '羊肉泡馍','壹只蟹蟹煲饭','香酥脆皮鸡米饭','广东煲仔饭','喵七公','马来一号',
             '京都牛肉盒子饭']       
    if 'M' in People:
        LunchList.remove('原素Essence西餐')
        LunchList.append('蜀道麻辣香锅')
        LunchList.append('小四川')
        LunchList.append('美味小厨')

    print ("We decided that today's lunch is .....")
    random.shuffle(LunchList)
    Item = random.choice(LunchList)
    print (Item)
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
