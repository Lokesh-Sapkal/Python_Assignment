##################################################################
##
##  Name :          Assignment_5_5X.py
##  Descirption :   Program to Check Even or Odd Number.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter three numbers: 17
Expected Output:
    17 is an odd number.
'''

def CheckEvenOdd(iNo):
    return ((iNo % 2) == 0)

def main():
    print("Enter the number : ")
    iValue = int(input())
    
    bRet = CheckEvenOdd(iValue)

    if(bRet == True):
        print(iValue,"is an even number.")
    else:
        print(iValue,"is an odd number")
    
if __name__ == "__main__":
    main()