def sum_of_array_elements(n, arr):
    total = 0
    while n>0:
        total=total+arr[n-1]
        n=n-1
    return total
    pass