# Input : 5
''' Output :    *   *   *    *   *
                *   *   *    *
                *   *   *
                *   *
                *                  '''

def Display(iNo):
    for i in range(1,iNo+1):
        for j in range(iNo,0,-1):
            if(i <= j):
                print("*\t",end="")
        print()

def main():
    print("Enter number: ")
    iValue = int(input())
    
    Display(iValue)

if __name__ == "__main__":
    main()