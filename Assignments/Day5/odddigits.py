def countOddDigits(n):
    count=0
    for digit in str(n):
        if int(digit)%2!=0:
            count=count+1
    return count
    pass