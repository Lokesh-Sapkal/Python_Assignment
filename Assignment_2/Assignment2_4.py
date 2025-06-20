# Input : 12
# Output : 16   (1+2+3+4+6)

def Display(iNo):
    iAns = 0
    for i in range(1,iNo):
        if((iNo % i) == 0):
            iAns = iAns + i
    
    return iAns

def main():
    print("Enter number: ")
    iValue = int(input())
    
    iRet = Display(iValue)

    print("Fctorial of number is",iRet)

if __name__ == "__main__":
    main()