def sumOfFrequencies(arr):
    count={}
    for num in arr:
        if num in count:
            count[num]+=1
        else:
            count[num]=1
    freq=list(count.values())
    highest=max(freq)
    lowest=min(freq)
    return highest+lowest
    pass