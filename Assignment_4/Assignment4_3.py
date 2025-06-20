'''
    Input List =        [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70] 
    List after filter = [76, 89, 86, 90, 70] 
    List after map =    [86, 99, 96, 100, 80] 
    Output of reduce =  6538752000
'''

from functools import reduce

ChkRange = lambda iNo1 : (iNo1 >= 70) & (iNo1 <= 90)

Increase = lambda iNo2: iNo2 + 10

Product = lambda A,B: A * B

def main():
    List = []

    print("Enter number of elements : ")
    iValue = int(input())

    print("Enter elements : ")
    for i in range(0,iValue):
        iValue = int(input())
        List.append(iValue)
    
    print("Input data: ",List)

    FData = list(filter(ChkRange,List))
    print("List after filter: ",FData)

    MData = list(map(Increase,FData))
    print("List after map: ",MData)

    RData = reduce(Product,MData)

    print("Product is : ",RData)

if __name__ == "__main__":
    main()