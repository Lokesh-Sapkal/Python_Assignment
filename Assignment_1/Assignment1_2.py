def ChkNum(number):
    if number % 2 == 0:
        return 1
    else:
        return 0

def main():
    print("Enter the Number: ")
    no1 = int(input())

    Ans = ChkNum(no1)

    if Ans == 1:
        print("Number is even")
    else:
        print("Number is odd")

if __name__=="__main__":
    main()