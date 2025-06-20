'''
    Input : Number of elements : 7
    Input Elements : 13  5   45  7   4   56  34
    Output : 56
'''

def FindMaximum(iNum):
    iMax = 0
    Data = []

    print("Enter elements: ")
    for i in range(0,iNum):
        iValue = int(input())
        Data.append(iValue)
        if(iMax < Data[i]):
            iMax = Data[i]

    return iMax

def main():
    iRet = 0
    iNo = 0

    print("Enter Number of elements : ")
    iNo = int(input())

    iRet = FindMaximum(iNo)

    print("Maximum number from the list is: ",iRet)

if __name__ == "__main__":
    main()