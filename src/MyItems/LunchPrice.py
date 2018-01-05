import os

def CalcPrice(Price,People,DFee,Discount,c):
    if c == '1':
        print("The price after discount is : " + str(format(float(Price) + float(DFee)/float(People) - float(Discount)/float(People),'.2f') ))
    elif c == '2':
        print("The average price is : " + str(format(float(Price)/float(People),'.2f') ))
    print("                      ")
    CoutinueOrExit()

def Main():
    while 1:
        c = input("""
1 -- Calculate single price
2 -- Calculate average price

Please input:  """)
        print("                      ")
        if not c.strip():
            print("Cannot input empty infos , pleae input again")
        else:
            if c == '1':
                while 1:
                    Price = input("Please input original price: ")
                    if Price.isalpha():
                        print("It is not a number , pleae input again")
                    elif not Price.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                       break

                while 1:
                    People = input("Please input number of people: ")
                    if People.isalpha():
                        print("It is not a number , pleae input again")
                    elif not People.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                        break
                
                while 1:
                    DFee = input("Please input delivery fee: ")
                    if DFee.isalpha():
                        print("It is not a number , pleae input again")
                    elif not DFee.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                        break

                while 1:
                    Discount = input("Please input total discount price: ")
                    if Discount.isalpha():
                        print("It is not a number , pleae input again")
                    elif not Discount.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                        break
                break
        
            elif c == '2':
                DFee = 0
                Discount = 0
                while 1:
                    Price = input("Please input price: ")
                    if Price.isalpha():
                        print("It is not a number , pleae input again")
                    elif not Price.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                       break

                while 1:
                    People = input("Please input number of people: ")
                    if People.isalpha():
                        print("It is not a number , pleae input again")
                    elif not People.strip():
                        print("Cannot input empty infos , pleae input again")
                    else:
                        break
                break

            else:
                print("Illegal number , please input again")

    print("                      ")
    CalcPrice(Price,People,DFee,Discount,c)
    

def CoutinueOrExit():
    while 1:
        cc = input("Coutinue Or Exit? (Y/N) ")
        if cc.lower() == 'y':
            Main()
        elif cc.lower() == 'n':
            exit(1)
        
if __name__ == '__main__':
    Main()

