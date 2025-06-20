'''
    Input : Number of elements : 11
    Input Elements : 13  5   45  7  4   56  5   34  2   5   65
    Element to search : 5
    Output : 3
'''

def Search(iNum,iEle):
    iCount = 0
    Data = []

    print("Enter elements: ")
    for i in range(0,iNum):
        iValue = int(input())
        Data.append(iValue)
        if(Data[i] == iEle):
            iCount = iCount + 1

    return iCount


def main():
    iFrq = 0
    iNo1 = 0
    iNo2 = 0

    print("Enter Number of elements : ")
    iNo1 = int(input())

    print("Enter element to search: ")
    iNo2 = int(input())

    iFrq = Search(iNo1,iNo2)

    print("Frequency of",iNo2,"in list is:",iFrq)

if __name__ == "__main__":
    main()