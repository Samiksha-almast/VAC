def isArmstrong(n):
    s=str(n)
    p=len(s)
    total=sum(int(d)**p for d in s)
    return total==n
    pass