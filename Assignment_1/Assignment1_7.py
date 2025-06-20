def ChkNum(number):
    if number % 5 == 0:
        return True
    else:
        return False

def main():
    print("Enter the Number: ")
    no1 = int(input())

    Ans = ChkNum(no1)

    if Ans == True:
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

if __name__=="__main__":
    main()