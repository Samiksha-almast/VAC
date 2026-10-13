def countprime(n):
    count=1
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,i**0.5):
            if i%j==0:
                is_prime=False
            break
        if is_prime:
            count=count+1
        return count