##############################################################
##
##  Name :          Assignment_6_5.py
##  Descirption :   Program to check whether no. is prime or not.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##############################################################

'''
Expected Input:
    Enter a number: 11
Expected Output
    11 is a prime number.
'''

def Prime(iNo):
    bAns = True

    for No in range(2,iNo):
        if((iNo % No) == 0):
            bAns = False
            break

    return bAns

def main():
    print("Enter a number : ")
    iValue = int(input())
    
    bRet = Prime(iValue)

    if(bRet == True):
        print(iValue,"is a prime number.")
    else:
        print(iValue,"is not a prime number.")

if __name__ == "__main__":
    main()