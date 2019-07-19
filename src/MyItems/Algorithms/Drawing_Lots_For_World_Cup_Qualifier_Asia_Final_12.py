import os
import random

def Main():
    DrawingLots()

def DrawingLots():
    print ("===================================================================================")

    TeamList = ['Iran','Japan','South Korea','Australia','Qatar','United Arab Emirates','Saudi Arabia','China PR','Iraq','Uzbekistan','Syria','Thailand']
    
    GroupA = []
    GroupB = []

    AGroup(TeamList,GroupA)
    BGroup(TeamList,GroupB)
    
    print ("Group A: "+ ' , '.join(GroupA))
    print ("Group B: "+ ' , '.join(GroupB))
    print ("===================================================================================")
    ChooseAgain()
    
def AGroup(TeamList,GroupA):
    for i in range(0,6):
        Team = random.choice(TeamList)
        GroupA.append(Team)
        TeamList.remove(Team)

def BGroup(TeamList,GroupB):
    for i in range(0,6):
        Team = random.choice(TeamList)
        GroupB.append(Team)
        TeamList.remove(Team)



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
