##################################################################
##
##  Name :          Assignment_5_1.py
##  Descirption :   Program to perform Arithmetic Operations on Two Numbers
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter first number:  10  
    Enter second number: 2
Expected Output:
    Sum:        12  
    Difference: 8  
    Product:    20  
    Division:   5.0
'''

def Summation(iValue1,iValue2):
    return iValue1 + iValue2

def Difference(iValue1,iValue2):
    return iValue1 - iValue2

def Product(iValue1,iValue2):
    return iValue1 * iValue2

def Division(iValue1,iValue2):
    return iValue1 / iValue2

def main():
    print("Enter first number : ")
    iNo1 = int(input())
    
    print("Enter second number : ")
    iNo2 = int(input())

    iSum = Summation(iNo1,iNo2)
    iDiff = Difference(iNo1,iNo2)
    iProd = Product(iNo1,iNo2)
    iDiv = Division(iNo1,iNo2)

    print("Sum : ",iSum)
    print("Difference : ",iDiff)
    print("Product : ",iProd)
    print("Division : ",iDiv)

if __name__ == "__main__":
    main()