##############################################################################
##
##  Name :          Assignment_6_3.py
##  Descirption :   Program to print accepted no's multiplication table up to 10.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################################

'''
Expected Input:
    Enter a number: 7
Expected Output
    7 x 1 = 7  
    7 x 2 = 14  
    ...  
    7 x 10 = 70
'''

def MultiTable(iNo):

    for No in range(1,11):
        iAns = iNo * No
        print(iNo,"*",No,"=",iAns)

def main():
    print("Enter the number : ")
    iValue = int(input())
    
    MultiTable(iValue)

if __name__ == "__main__":
    main()