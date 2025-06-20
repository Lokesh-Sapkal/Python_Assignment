def Add(num1):
    if num1 > 0:
        return 0
    elif num1 < 0:
        return 1
    else:
        return 2

def main():
    print("Enter no1 : ")
    no1 = int(input())

    Ret = Add(no1)

    if Ret == 0:
        print("Number is positive")
    elif Ret == 1:
        print("Number is negative")
    else:
        print("Number is Zero")

if __name__=="__main__":
    main()