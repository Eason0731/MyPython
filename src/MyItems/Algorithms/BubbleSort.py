import os

def BubbleSortbyASC(List):
    for i in range(0,len(List)):
        for j in range(i+1,len(List)):
            if List[i] > List[j]:
                temp = List[i] 
                List[i] = List[j]
                List[j] = temp

    print ("The result of bubble sort order by ASC is: " + str(List))
    
def BubbleSortbyDESC(List):
    for i in range(0,len(List)):
        for j in range(i+1,len(List)):
            if List[i] < List[j]:
                temp = List[i] 
                List[i] = List[j]
                List[j] = temp

    print ("The result of bubble sort order by DESC is: " + str(List))

def BubbleSortbyCutsom(Number):
    List = []
    for i in range(0,int(Number)):
        ListNum = input("Please input the number " + str(i+1)+ ":")
        if (ListNum.startswith('-') and ListNum[1:] or ListNum).isdigit():
            List.append(int(ListNum))
        else:
            print (ListNum + " is a illegeal number and won't add it to the list!")
    BubbleSortbyASC(List)
    BubbleSortbyDESC(List)
    
if __name__ == '__main__':
    Number = input("How many numbers do you want to input?")
    if Number.isdigit():
        BubbleSortbyCutsom(Number)
    else:
        print ("Cannot input illegal number ,please input again!")
