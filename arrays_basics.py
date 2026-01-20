# Q1. Do ALL of the following:
#    Given a list:
#    1. Print each element with its index 
#    2. Find the maximum number WITHOUT using max()
#    3. Count how many times 1 appears WITHOUT using count()

nums = [3,1,4,1,5]
for i in range(len(nums)):
    print(f"Index {i} -> {nums[i]}")

max_val = nums[0]
for i in nums:
    if i > max_val:
        max_val = i
print('Max Value is:',max_val)

count = 0
for i in nums:
    if i == 1:
        count+=1
print('1 has appeared:',count,'times')