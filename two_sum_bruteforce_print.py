# Q2. You have this:

# nums = [2, 7, 11, 15]
# target = 9
# Your job is to:
    # Pick one number
    # Pick another number after it
    # Add them
    # Check if the sum equals target
    # If yes → return their indices

nums = [2, 7, 11, 15]
target = 9
found = False

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print('The two index are:',i,j)
            found = True
    if found:
        break

if not found:
    print('No Possible Outcomes')
