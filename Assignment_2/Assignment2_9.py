# Input : 5187934
# Output : 7

def CountDigit(iNo):
    iCount = 0
    while(iNo != 0):
        iNo = int(iNo / 10)
        iCount = iCount + 1
    
    return iCount

def main():
    print("Enter number: ")
    iValue = int(input())
    
    iRet = CountDigit(iValue)

    print("Total digit in the ",iValue," is : ",iRet)

if __name__ == "__main__":
    main()