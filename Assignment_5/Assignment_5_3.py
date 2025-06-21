##################################################################
##
##  Name :          Assignment_5_3.py
##  Descirption :   Program to Check Vowel or Consonant.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter age: 19
Expected Output:
    Eligible to vote.
'''

def CheckAge(iNo):
    if(iNo >= 18):
        return True
    else:
        return False

def main():
    print("Enter the Age: ")
    iValue = int(input())
    
    bRet = CheckAge(iValue)

    if(bRet == True):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")
    
if __name__ == "__main__":
    main()