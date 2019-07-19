import os
import random

def Main():
    DrawingLots()

def DrawingLots():
    print ("===================================================================================")

    FirstClass = ['IR Iran','Japan','Korea Republic','Australia','Qatar','UAE','Saudi Arabia','China PR']
    SecondClass = ['Iraq','Uzbekistan','Syria','Oman','Lebanon','Kyrgyz Republic','Vietnam','Jordan']
    ThirdClass = ['Palestine','India','Bahrain','Thailand','Tajikistan','Korea DPR','Chinese Taipei','Philippines']
    FourthClass = ['Turkmenistan','Myanmar','Hong Kong','Yemen','Afghanistan','Maldives','Kuwait','Malaysia']
    FifthClass = ['Indonesia','Singapore','Nepal','Cambodia','Bangladesh','Mongolia','Guam','Sri Lanka']
    
    GroupA = []
    GroupB = []
    GroupC = []
    GroupD = []
    GroupE = []
    GroupF = []
    GroupG = []
    GroupH = []
    
    FirstClassTeam(FirstClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH)
    SecondClassTeam(SecondClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH)
    ThirdClassTeam(ThirdClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH)
    FourthClassTeam(FourthClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH)
    FifthClassTeam(FifthClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH)

    print ("Group A: "+ ' , '.join(GroupA))
    print ("Group B: "+ ' , '.join(GroupB))
    print ("Group C: "+ ' , '.join(GroupC))
    print ("Group D: "+ ' , '.join(GroupD))
    print ("Group E: "+ ' , '.join(GroupE))
    print ("Group F: "+ ' , '.join(GroupF))
    print ("Group G: "+ ' , '.join(GroupG))
    print ("Group H: "+ ' , '.join(GroupH))
    print ("===================================================================================")
    ChooseAgain()
    
def FirstClassTeam(FirstClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH):
    Team = random.choice(FirstClass)
    GroupA.append(Team)
    FirstClass.remove(Team)
        
    Team = random.choice(FirstClass)
    GroupB.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupC.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupD.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupE.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupF.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupG.append(Team)
    FirstClass.remove(Team)

    Team = random.choice(FirstClass)
    GroupH.append(Team)
    FirstClass.remove(Team)

def SecondClassTeam(SecondClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH):
    Team = random.choice(SecondClass)
    GroupA.append(Team)
    SecondClass.remove(Team)
        
    Team = random.choice(SecondClass)
    GroupB.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupC.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupD.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupE.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupF.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupG.append(Team)
    SecondClass.remove(Team)

    Team = random.choice(SecondClass)
    GroupH.append(Team)
    SecondClass.remove(Team)

def ThirdClassTeam(ThirdClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH):
    Team = random.choice(ThirdClass)
    GroupA.append(Team)
    ThirdClass.remove(Team)
        
    Team = random.choice(ThirdClass)
    GroupB.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupC.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupD.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupE.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupF.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupG.append(Team)
    ThirdClass.remove(Team)

    Team = random.choice(ThirdClass)
    GroupH.append(Team)
    ThirdClass.remove(Team)

def FourthClassTeam(FourthClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH):
    Team = random.choice(FourthClass)
    GroupA.append(Team)
    FourthClass.remove(Team)
        
    Team = random.choice(FourthClass)
    GroupB.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupC.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupD.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupE.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupF.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupG.append(Team)
    FourthClass.remove(Team)

    Team = random.choice(FourthClass)
    GroupH.append(Team)
    FourthClass.remove(Team)

def FifthClassTeam(FifthClass,GroupA,GroupB,GroupC,GroupD,GroupE,GroupF,GroupG,GroupH):
    Team = random.choice(FifthClass)
    GroupA.append(Team)
    FifthClass.remove(Team)
        
    Team = random.choice(FifthClass)
    GroupB.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupC.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupD.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupE.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupF.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupG.append(Team)
    FifthClass.remove(Team)

    Team = random.choice(FifthClass)
    GroupH.append(Team)
    FifthClass.remove(Team)


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
