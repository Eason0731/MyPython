import os

def Main():
    Year = input("Please input year: ")
    if not Year.strip():
        print ("Cannot input empty infos")
        Continue()
    else:
        if Year.isdigit():
            if int(Year) > 0:
                LeapYear(Year)
        else:
            print ("Cannot input illegal year, please input again")
            Continue()
        
def LeapYear(Year):
    if int(Year) % 4 == 0 and int(Year) % 100 != 0 or int(Year) % 100 == 0 and int(Year) % 400 == 0:
        print (Year + " is leap year!")
    else:
        print (Year + " is NOT leap year!")
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
    
                
        
    
