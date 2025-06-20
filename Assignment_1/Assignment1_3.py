def Add(num1,num2):
    Ans = num1 + num2
    return Ans

def main():
    print("Enter no1 : ")
    no1 = int(input())
    print("Enter no2 : ")
    no2 = int(input())

    Ret = Add(no1,no2)

    print("Addition is : ",Ret)

if __name__=="__main__":
    main()