def first_last6(nums):
    if nums[0]==6 or nums[(len(nums)-1)]==6:
        return True
    else:
        return False

def same_first_last(nums):
    if len(nums)>1 and nums[0]==nums[(len(nums)-1)]:
        return True
    elif len(nums)==1:
        return True
    else:
        return False

def make_pi():
    return [3,1,4]

def common_end(a,b):
    if a[0]==b[0]:
        return True
    elif a[(len(a)-1)] == b[(len(b)-1)]:
        return True
    else:
        return False
    
def sum3(nums):
    if (len(nums)==3):
        return sum(nums)
    
def rotate_left3(nums):
    first=nums[0]
    nums.remove(nums[0])
    nums.append(first)
    return nums

def reverse3(nums):
   nums.reverse()
   return nums

def max_end3(nums):
    a=max(nums[0],nums[len(nums)-1])
    for i in range(len(nums)):
        nums[i]=a
    return nums

def sum2(nums):
  if len(nums)>=2:
    return nums[0] + nums [1]
  elif len(nums)<2:
    return sum(nums)
  else:
    return 0

def middle_way(a,b):
    c=[]
    c=[a[1],b[1]]
    return c

def make_ends(nums):
    news=[nums[0],nums[(len(nums)-1)]]
    return news

def has23(nums):
    if (2 in nums) or (3 in nums):
        return True
    else:
        return False