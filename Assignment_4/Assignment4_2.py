'''
    Input : 4   3
    Output : 12
    
    Input : 6   3
    Output : 18
'''

Multiplicatoin = lambda No1,No2 : No1 * No2

def main():
    print("Enter first number : ")
    iValue1 = int(input())

    print("Enter first number : ")
    iValue2 = int(input())
    
    iRet = Multiplicatoin(iValue1,iValue2)

    print("Multiplication of",iValue1,"and",iValue2,"is:",iRet)

if __name__ == "__main__":
    main()
    