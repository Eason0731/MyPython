import os
import re

def Main():
    Principal = input("Please input principal: ")
    Days = input("Please input expected days: ")
    Rate = input("Please input annual interest rate: ")

    RegexFloat = re.compile(r"^(-?\d+)(\.\d*)?$")
    RegexInt = re.compile(r"^(-?\d+)(\d*)?$")
    if re.match(RegexFloat,Principal) and re.match(RegexInt,Days) and re.match(RegexFloat,Rate):
        if float(Principal) > 0 and int(Days) > 0 and float(Rate) > 0:
            CalcInterestAndAccumulatedAmount(float(Principal),int(Days),float(Rate))
        else:
            print ("Cannot input negative number, please input again")
            Continue()
    else:
        print ("Cannot input illegal number, please input again")
        Continue()
                    
def CalcInterestAndAccumulatedAmount(Principal,Days,Rate):
    Rate = (Rate/100)
    Interest = (Principal*Days*Rate)/365
    print ("======================================================")
    print ("Interest after "+ str(Days) +" days are %.2f" %(Interest) + " yuan")
    print ("Accumulated amount are %.2f" %(Principal+Interest) + " yuan")
    print ("======================================================")
    Continue()
    
def Continue():
    while(1):
        IsContinue = input("Continue or Not?(Y/N)")
        if not IsContinue.strip():
            print ("Cannot input empty infos, please input again")
        else:
            print ("                                 ")
            if IsContinue.upper() == 'Y':
                Main()
            elif IsContinue.upper() == 'N':
                exit(1)
            else:
                print ("Cannot input illegal character, please input again")
   

if __name__ == '__main__':
    Main()
    
                
        
    
