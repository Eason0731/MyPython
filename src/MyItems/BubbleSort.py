import os

def BubbleSortbyASC():
    List = [21,8,5,1,7,3,14]  
    for i in range(0,len(List)):
        for j in range(i+1,len(List)):
            if List[i] > List[j]:
                temp = List[i] 
                List[i] = List[j]
                List[j] = temp

    print (List)
    
def BubbleSortbyDESC():
    List = [21,8,5,1,7,3,14]  
    for i in range(0,len(List)):
        for j in range(i+1,len(List)):
            if List[i] < List[j]:
                temp = List[i] 
                List[i] = List[j]
                List[j] = temp

    print (List)
    
if __name__ == '__main__':
    BubbleSortbyASC()
    BubbleSortbyDESC()
