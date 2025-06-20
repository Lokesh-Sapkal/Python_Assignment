'''
    Input : 4
    Output : 16

    Input : 6
    Output : 64
'''

Power = lambda iNo: iNo ** 2

def main():
    print("Enter number : ")
    iValue = int(input())

    iRet = Power(iValue)

    print("Power of",iValue,"is :",iRet)

if __name__ == "__main__":
    main()