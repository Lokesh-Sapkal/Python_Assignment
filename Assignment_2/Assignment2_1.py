import Arithmetic

def main():
    print("Enter first number: ")
    iValue1 = int(input())
    
    print("Enter second number: ")
    iValue2 = int(input())

    iRet = Arithmetic.Add(iValue1,iValue2)
    print("Addition is : ",iRet)
    
    iRet = Arithmetic.Sub(iValue1,iValue2)
    print("Subtraction is : ",iRet)
    
    iRet = Arithmetic.Mult(iValue1,iValue2)
    print("Multiplication is : ",iRet)
    
    iRet = Arithmetic.Div(iValue1,iValue2)
    print("Division is : ",iRet)

if __name__ == "__main__":
    main()
