# Input : 5187934
# Output : 37

def AddDigit(iNo):
    iAdd = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = (iNo % 10)
        iAdd = iAdd + iDigit
        iNo = int(iNo / 10)
    
    return iAdd

def main():
    print("Enter number: ")
    iValue = int(input())
    
    iRet = AddDigit(iValue)

    print("Addition of digit in the ",iValue," is : ",iRet)

if __name__ == "__main__":
    main()