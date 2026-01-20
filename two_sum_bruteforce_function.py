# Q3. 
# nums = [2, 7, 11, 15]
# target = 9
# You must:
# 1.Write a function
# 2.Use the same brute-force logic
# 3.Return the indices (not print)
# 4.Return None if no pair exists
# 5.Do NOT use found
# 6.Do NOT use dictionary yet

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
            
    return None
            
print(two_sum([2,11,7,3],9))
