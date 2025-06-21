##############################################################
##
##  Name :          Assignment_6_7.py
##  Descirption :   Program to Print  the largest number.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################

'''
Expected Input:
    Enter 5 numbers: 23 89 12 56 45
Expected Output:
    Maximum number is: 89
'''

def Maximum(iNo):
    iMax = 0

    for i in iNo:
        if(iMax < i):
            iMax = i

    return iMax

def main():
    print("Enter 5 numbers : ")
    List = []

    for i in range(0,5):
        iValue = int(input())
        List.append(iValue)
    
    iRet = Maximum(List)

    print("Maximum number is : ",iRet)

if __name__ == "__main__":
    main()