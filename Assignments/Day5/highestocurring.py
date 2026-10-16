def highestOccurringElement(nums):
    highest=nums[0]
    max_count=0
    for num in nums:
        count=nums.count(num)
        if count>max_count:
            max_count=count
            highest=num
    return highest
    pass