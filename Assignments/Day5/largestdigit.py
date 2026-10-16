def returnLargestDigit(n):
    largest=0
    for digit in str(n):
        if int(digit)>largest:
            largest=int(digit)
    return largest
    pass