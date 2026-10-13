def returnLargestDigit(n):
    largest=0
    for digit in str(n):
        d=int(digit)
        if d>largest:
            largest=d
    return largest