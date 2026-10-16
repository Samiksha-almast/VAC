def isArmstrong(n):
    digits=str(n)
    power=len(digits)
    total=0
    for digit in digits:
        total=total+int(digit)**power
    return total==n
    pass