'''
    Input : Number of elements : 11
    Input Elements : 13  5   45  7  4   56  10   34  2   5   8
    Output : 32 (13 + 5 + 7 + 2 + 5)
'''
import MarvellousNum as ms

def ListPrime(iNum):
    iAdd = 0
    iAns = 0
    Data = []

    print("Enter elements: ")
    for i in range(0,iNum):
        iValue = int(input())
        Data.append(iValue)
        
        iAns = ms.ChkPrime(Data[i])

        if(iAns == None):
            iAns = 0

        iAdd = iAdd + iAns

    return iAdd

def main():
    iRet = 0
    iNo = 0

    print("Enter Number of elements : ")
    iNo = int(input())

    iRet = ListPrime(iNo)

    print("Addition of all prime no. from list is:",iRet)

if __name__ == "__main__":
    main()