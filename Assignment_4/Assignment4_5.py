'''
    Input List =        [2, 70 , 11, 10, 17, 23, 31, 77] 
    List after filter = [2, 11, 17, 23, 31] 
    List after map =    [4, 22, 34, 46, 62] 
    Output of reduce =  62
'''
from functools import reduce

def Prime(value):
    bValue = True

    for i in range(2,value):
        if((value % i) == 0):
            return False
            break

    return bValue

Multi = lambda a : a * 2

def Max(No1,No2):
    # iMax = 0

    # for i in No:
    if(No1 < No2):
        No1 = No2

    return No1

def main():
    List = []

    print("Enter the size : ")
    iSize = int(input())
 
    print("Enter the elements : ")
    for i in range(0,iSize):
        data = int(input())
        List.append(data)

    print("Input List : ",List)

    Fdata = list(filter(Prime,List))

    print("List after filter : ",Fdata)

    Mdata = list(map(Multi,Fdata))

    print("List after map : ",Mdata)

    Rdata = reduce(Max,Mdata)

    print("Output of reduce : ",Rdata)

if __name__ == "__main__":
    main()