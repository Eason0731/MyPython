import os
import re

def MainFunction():
    while(1):
        A = input ("Please input the first edge: ")
        B = input ("Please input the second edge: ")
        C = input ("Please input the third edge: ")
    
        Regex = re.compile(r"^(-?\d+)(\.\d*)?$")
        if re.match(Regex,A) and re.match(Regex,B) and re.match(Regex,C):
            if float(A) >= 0 and float(B) >= 0 and float(C) >= 0:
                Triangle(float(A),float(B),float(C))
                break
            else:
                print ("The value of edge cannot be negative number ,please input again!")
                print ("                             ")
        else:
            print ("The value of edge is not a number,please input again!")
            print ("                             ")


def Triangle(A,B,C):
    if A+B>C and A+C>B and B+C>A:
        if A==B==C:
            print ("This is an equilateral triangle")
        elif A==B or A==C or B==C:
            print ("This is an isosceles triangle")
        elif pow(A,2)+pow(B,2)==pow(C,2) or pow(A,2)+pow(C,2)==pow(B,2) or pow(B,2)+pow(C,2)==pow(A,2):
            print ("This is a right triangle")
        elif (A== B and pow(A,2)+pow(B,2)==pow(C,2)) or (A==C and pow(A,2)+pow(C,2)==pow(B,2)) or (B==C and pow(B,2)+pow(C,2)==pow(A,2)):
            print ("This is an isosceles right angle triangle")
        else:
            print ("This is an ordinary triangle")
    else:
        print ("Cannot build a triangle")
    Continue()

def Continue():
    while(1):
        IsContinue = input("Continue or not?(Y/N) ")
        if IsContinue.upper() == 'Y':
            MainFunction()
        elif IsContinue.upper() == 'N':
            exit(1)
        else:
            print ("Do not input illegal character, please input again!")

if __name__ == '__main__':
    MainFunction()
        
