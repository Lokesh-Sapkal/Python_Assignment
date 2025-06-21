##################################################################
##
##  Name :          Assignment_5_7.py
##  Descirption :   Program to Calculate Area and Perimeter of Rectangle.
##  Author :        Lokesh Sanjay Sapkal
##  Date :          20-06-2025
##
##################################################################

'''
Expected Input:
    Enter length: 5  
    Enter width: 3
Expected Output:
    Area: 15  
    Perimeter: 16
'''

def Calculate(iLength,iWidth):
    
    fArea = iLength * iWidth

    fPerimeter = 2 * (iLength + iWidth)

    return fArea , fPerimeter

def main():
    print("Enter length : ")
    iLen = int(input())
    
    print("Enter width : ")
    iWid = int(input())
    
    fRet1 , fRet2 = Calculate(iLen,iWid)

    print("Area of Rectangle : ",fRet1)
    
    print("Perimeter of Rectangle : ",fRet2)
    
if __name__ == "__main__":
    main()