# Input : 5
# Output : 120

def Display(iNo):
    iAns = 1
    for i in range(1,iNo+1):
        iAns = iAns * i
    
    return iAns

def main():
    print("Enter number: ")
    iValue = int(input())
    
    iRet = Display(iValue)

    print("Fctorial of number is",iRet)

if __name__ == "__main__":
    main()