##################################################################
##
##  Name :          Assignment_5_6.py
##  Descirption :   Program to Converter Celsius to Fahrenheit.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter temperature in Celsius : 25
Expected Output:
    Temperature in Fahrenheit : 77.0°F.
'''

def ConvertCeltoFeh(iNo):
    fAns = (iNo * (9/5)) + 32

    return fAns

def main():
    print("Enter temperature in Celsius : ")
    iCel = int(input())
    
    fRet = ConvertCeltoFeh(iCel)

    print("Temperature in Fahrenheit : ",fRet,"°F")
    
if __name__ == "__main__":
    main()