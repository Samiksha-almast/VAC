def secondHighestOccurringElement(arr):
    count={}
    for num in arr:
        if num in count:
            count[num]+=1
        else:
            count[num]=1

    freq=list(set(count.values()))
    freq.sort(reverse=True)

    if len(freq)<2:
        return-1
    second_freq=freq[1]
    result=[]

    for num in count:
        if count[num]==second_freq:
            result.append(num)
    return min(result)