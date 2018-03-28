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
    List1 = ['老广东','福荣祥烧腊','吉祥馄饨','原素Essence西餐','杨铭宇黄焖鸡米饭','东池便当','大阪牛肉饭','福客桂林米粉','杨国富麻辣烫']       
    if 'M' in People:
        List1.remove('原素Essence西餐')
        List1.append('蜀道麻辣香锅')
        List1.append('小四川')

    print ("We decided that today's lunch is .....")
    random.shuffle(List1)
    Item = random.choice(List1)
    print (Item)
    
if __name__ == '__main__':
    Main()
