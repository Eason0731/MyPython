import os
import re

def MainFunction():
    while(1):
        A = input ("请输入第一条边: ")
        B = input ("请输入第二条边: ")
        C = input ("请输入第三条边: ")
    
        Regex = re.compile(r"^(-?\d+)(\.\d*)?$")
        if re.match(Regex,A) and re.match(Regex,B) and re.match(Regex,C):
            if float(A) >= 0 and float(B) >= 0 and float(C) >= 0:
                Triangle(float(A),float(B),float(C))
                break
            else:
                print ("边不能负数,请重新输入!")
                print ("                             ")
        else:
            print ("其中有边的值不是数字,请重新输入!")
            print ("                             ")


def Triangle(A,B,C):
    if A+B>C and A+C>B and B+C>A:
        if A==B==C:
            print ("这是个等边三角形")
        elif A==B or A==C or B==C:
            print ("这是个等腰三角形")
        elif pow(A,2)+pow(B,2)==pow(C,2) or pow(A,2)+pow(C,2)==pow(B,2) or pow(B,2)+pow(C,2)==pow(A,2):
            print ("这是个直角三角形")
        elif A== B and pow(A,2)+pow(B,2)==pow(C,2) or A==C and pow(A,2)+pow(C,2)==pow(B,2) or B==C and pow(B,2)+pow(C,2)==pow(A,2):
            print ("这是个等腰直角三角形")
        else:
            print ("这是个普通三角形")
    else:
        print ("无法构成三角形")

if __name__ == '__main__':
    MainFunction()
        
