##################################################################
##
##  Name :          Assignment_6_1.py
##  Descirption :   Program to print numbers from 1 to 50.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Output:
    1 2 3 4 ... 50
'''

def main():
    iNo = 1
    while(iNo <= 50):
        print(iNo,"\t",end='')
        iNo = iNo + 1

if __name__ == "__main__":
    main()