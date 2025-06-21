##################################################################
##
##  Name :          Assignment_5_2.py
##  Descirption :   Program to Check Vowel or Consonant.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter a character: e
Expected Output:
    'e' is a vowel
'''

def CheckVowel(ch):
    # if((ch >= 'A') and (ch <= 'Z')):
        # ch = ch + 32

    if((ch == 'a') or (ch == 'u') or (ch == 'o') or (ch == 'i') or (ch == 'e')):
        return True
    else:
        return False

def main():
    print("Enter a character: ")
    cValue = str(input())
    
    bRet = CheckVowel(cValue)

    if(bRet == True):
        print(cValue,"is a vowel")
    else:
        print(cValue,"is not a vowel")
    
if __name__ == "__main__":
    main()