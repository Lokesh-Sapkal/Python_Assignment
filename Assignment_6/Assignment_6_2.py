##############################################################################
##
##  Name :          Assignment_6_2.py
##  Descirption :   Program to print the sum of all even numbers from 1 to 100.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################################

'''
Expected Output:
    Sum of even numbers between 1 to 100 is: 2550
'''

def SumEven():
    iSum = 0

    for No in range(1,101):
        if((No % 2) == 0):
            iSum = iSum + No

    return iSum

def main():
    
    iRet = SumEven()

    print("Sum of even numbers between 1 to 100 is : ",iRet)

if __name__ == "__main__":
    main()