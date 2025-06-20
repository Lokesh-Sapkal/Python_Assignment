def ChkPrime(iNo):
    iCnt = 0

    for i in range(2,iNo):
        if((iNo % i) == 0):
            iCnt = iCnt + 1

    if(iCnt == 0):
        return iNo