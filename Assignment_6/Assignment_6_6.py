##############################################################
##
##  Name :          Assignment_6_6.py
##  Descirption :   Program to Print Triangle Pattern.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################

'''
Expected Output
    *
    * *
    * * *
    * * * *
'''

def Pattern(iRow,iCol):

    if(iRow != iCol):
        return

    for i in range(0,iRow):
        for j in range(0,iCol):
            if(i >= j):
                print("*\t",end='')
        print()

def main():
    print("Enter number of rows : ")
    iValue1 = int(input())
    
    print("Enter number of columns : ")
    iValue2 = int(input())
    
    Pattern(iValue1,iValue2)

if __name__ == "__main__":
    main()