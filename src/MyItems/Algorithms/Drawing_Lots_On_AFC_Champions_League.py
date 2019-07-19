import os
import random

def Main():
    DrawingLots()

def DrawingLots():
    print ("===================================================================================")

    TeamList = ['Shanghai SIPG [CHN]','Guangzhou Evergrande [CHN]','Urawa Red Diamonds [JPN]','Kashima Antlers [JPN]']
    
    GroupA = []
    GroupB = []

    AGroup(TeamList,GroupA)
    BGroup(TeamList,GroupB)
    
    print ("East Asia Semi Final Zone 1: "+ '  VS   '.join(GroupA))
    print ("East Asia Semi Final Zone 2: "+ '  VS   '.join(GroupB))
    print ("===================================================================================")
    ChooseAgain()
    
def AGroup(TeamList,GroupA):
    for i in range(0,2):
        Team = random.choice(TeamList)
        GroupA.append(Team)
        TeamList.remove(Team)

def BGroup(TeamList,GroupB):
    for i in range(0,2):
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
