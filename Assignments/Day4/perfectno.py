def isPerfectNumber(n):
    if n<=1:
        return False
    total=0
    for i in range(1,n):
        if n%i==0:
            total=total+i
    if total==n:
        return True
    else:
        return False
    pass