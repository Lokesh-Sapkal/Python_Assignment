##############################################################
##
##  Name :          Assignment_6_4.py
##  Descirption :   Program to print accepted no's factorial.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################

'''
Expected Input:
    Enter a number: 5
Expected Output
    Factorial of 5 is: 120
'''

def Factorial(iNo):
    iFact = 1

    for No in range(1,iNo + 1):
        iFact = iFact * No

    return iFact

def main():
    print("Enter the number : ")
    iValue = int(input())
    
    iRet = Factorial(iValue)

    print("factorial of",iValue,"is : ",iRet)

if __name__ == "__main__":
    main()