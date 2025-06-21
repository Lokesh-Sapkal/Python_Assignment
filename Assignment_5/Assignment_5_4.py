##################################################################
##
##  Name :          Assignment_5_4.py
##  Descirption :   Program to Find Largest Among Three Numbers .
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter three numbers: 5 9 3
Expected Output:
    Largest number is 9.
'''

def CheckMax(iNo1,iNo2,iNo3):
    if((iNo1 > iNo2) and (iNo1 > iNo3)):
        return iNo1
    elif(iNo2 > iNo3):
        return iNo2
    else:
        return iNo3

def main():
    print("Enter first number : ")
    iValue1 = int(input())
    
    print("Enter second number : ")
    iValue2 = int(input())
    
    print("Enter third number : ")
    iValue3 = int(input())
    
    iRet = CheckMax(iValue1,iValue2,iValue3)

    print("Largest number : ",iRet)
    
if __name__ == "__main__":
    main()