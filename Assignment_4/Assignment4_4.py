'''
    Input List =        [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
    List after filter = [2, 4, 4, 2, 8, 10] 
    List after map =    [4, 16, 16, 4, 64, 100] 
    Output of reduce =  204 
'''

from functools import reduce

Even = lambda a : (a % 2) == 0

Square = lambda p : p ** 2

Add = lambda x,y : x + y

def main():
    List = []

    print("Enter the size : ")
    iSize = int(input())

    print("Enter the elements : ")
    for i in range(0,iSize):
        data = int(input())
        List.append(data)

    print("Input List : ",List)

    Fdata = list(filter(Even,List))

    print("List after filter : ",Fdata)

    Mdata = list(map(Square,Fdata))

    print("List after map : ",Mdata)

    Rdata = reduce(Add,Mdata)

    print("Output of reduce is : ",Rdata)

if __name__ == "__main__":
    main()