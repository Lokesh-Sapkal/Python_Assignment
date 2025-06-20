'''
    Input : Number of elements : 6
    Input Elements : 13  5   45  7   4   56
    Output : 130
'''

def Addition(iNum):
    iAdd = 0
    Data = []

    print("Enter elements: ")
    for i in range(0,iNum):
        iValue = int(input())
        Data.append(iValue)
        iAdd = iAdd + Data[i]

    return iAdd

def main():
    iRet = 0
    iNo = 0

    print("Enter Number of elements : ")
    iNo = int(input())

    iRet = Addition(iNo)

    print("Addition is: ",iRet)

if __name__ == "__main__":
    main()