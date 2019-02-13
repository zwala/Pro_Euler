
def count_evens(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1
    return count

def big_diff(nums):
    small=min(nums)
    big=max(nums)
    return big-small

def centered_average(nums):
    small=min(nums)
    big=max(nums)
    nums.remove(small)
    nums.remove(big)
    average=sum(nums) / len(nums)
    return average

def sum13(nums):
    count = 0
    while count < len(nums):
        if nums[count] == 13:
            del nums[count:count+2]
            continue
        count += 1
    return sum(nums)

def sum67(nums):
    key=0
    add=0
    for each in nums:
        if key==0:
            if each==6:
                key=1
            else:
                add=add+each
        else:
            if each==7:
                key=0
    return add

def has22(nums):
    key=0
    for i in range(len(nums)-1):
        if nums[i]==2 and nums[i+1]==2:
            key+=1
    if key==0:
        return False
    else:
        return True