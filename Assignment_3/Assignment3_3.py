'''
    Input : Number of elements : 4
    Input Elements : 13  5   45  7
    Output : 5
'''

def FindMinimum(iNum):
    iMin = 0
    Data = []

    print("Enter elements: ")
    for i in range(0,iNum):
        iValue = int(input())
        Data.append(iValue)
        if(Data[i] == Data[0]):
            iMin = Data[i]
        if(iMin > Data[i]):
            iMin = Data[i]

    return iMin

def main():
    iRet = 0
    iNo = 0

    print("Enter Number of elements : ")
    iNo = int(input())

    iRet = FindMinimum(iNo)

    print("Minimum number from the list is: ",iRet)

if __name__ == "__main__":
    main()