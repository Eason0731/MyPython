import re
import os
import math

def Main():
    a = input("Please input the first number: ")
    b = input("Please input the second number: ")
    c = input("Please input the third number: ")

    if not a.strip() or not b.strip() or not c.strip():
        print ("Please do not input empty infos!")
        Countinue()
    else:
        Regex = re.compile(r"^(-?\d+)?$")
        if re.match(Regex,a) and re.match(Regex,b) and re.match(Regex,c):
            if int(a) < 0:
                print ("Please do not input the first number " + a + " less than 0" )
                Countinue()
            else:
                Quadratic(int(a),int(b),int(c))
        
        else:
            print ("Please do not input non-numeric on it!")
            Countinue()


def Quadratic(a,b,c):
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print ("There is no real root on this quadratic")
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print ("")
        print ("The first root of this quadratic is: " + str(x1))
        print ("The second root of this quadratic is: " + str(x2))
        Countinue()

def Countinue():
    print ("")
    while(1):
        IsCountinue = input ("Countinue or Not? (Y/N) ")
        if IsCountinue.upper() == 'Y':
            Main()
        elif IsCountinue.upper() == 'N':
            exit(1)
        else:
            print ("Do not input illegal character, please input again!")
    
        

if __name__ == '__main__':
    Main()
    
