# Q1. Do ALL of the following:
#    Given a list:
#    1. Print each element with its index 
#    2. Find the maximum number WITHOUT using max()
#    3. Count how many times 1 appears WITHOUT using count()

nums = [3,1,4,1,5]
for i in range(len(nums)):
    print(f'Element {i} -> {nums[i]}')

max_num = nums[0]
for a in range(len(nums)):
    if nums[a] > max_num:
        max_num = nums[a]
print(f'The Maximum Number is {max_num}')

count = 0
for c in range(len(nums)):
    if nums[c] == 1:
        count+=1
print(f'1 has appeared: {count} times')