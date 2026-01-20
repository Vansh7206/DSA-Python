# Q4. nums = [2, 11, 7, 3]
#     target = 9
# 1. Requirements (strict):
# 2. Use ONLY while loops
# 3. Use two pointers (i and j)
# 4. Return indices, not values
# 5. Return None if no pair exists
# 6. NO dictionary
# 7. NO for loop
# 8. NO print inside logic

def two_sum(nums,target):
    i = 0
    while i < len(nums):
        j = i + 1
        while j <len(nums):
            if nums[i] + nums[j] == target:
                return i,j
            j+=1
        i+=1
    return None
print(two_sum([2,7,5,11],9))
