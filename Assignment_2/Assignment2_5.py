# Input : 5
# Output : It is Prime Number

def ChkPrime(iNo):
    iAns = False
    for i in range(2,iNo):
        if((iNo % i) == 0):
            iAns = True
    
    return iAns

def main():
    print("Enter number: ")
    iValue = int(input())
    
    iRet = ChkPrime(iValue)

    if(iRet == False):
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()