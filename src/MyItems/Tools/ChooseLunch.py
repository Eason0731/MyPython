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
            People = 'S'
            ChooseLunch(People)
            break
        elif People == '2':
            People = 'M'
            ChooseLunch(People)
            break
        else:
            print ("Do not input illegal number, please input again!")

def ChooseLunch(People):
    if 'S' in People:
        List1 = ['老广东','福荣祥','吉祥馄饨','原素西餐','黄焖鸡米饭','东池便当','大板牛肉饭']
    elif 'M' in People:
        List1 = ['麻辣香锅','黄焖鸡米饭','老广东','福荣祥']

    print ("We decided that today's lunch is .....")
    random.shuffle(List1)
    Item = random.choice(List1)
    print (Item)
    
if __name__ == '__main__':
    Main()
