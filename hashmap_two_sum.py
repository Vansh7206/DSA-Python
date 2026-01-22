# Q5. nums = [2, 7, 11, 15]
# target = 9
# Example:
# Current number = 7
# Target = 9
# Needed = 9 - 7 = 2
# If 2 was seen before → solution found.
# Requirements (strict):
# Use a dictionary
# One loop only
# Return indices
# No nested loops
# No prints inside logic
# Return None if no pair exists

def two_sum(nums,target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                  return seen[needed],i
            else:
                seen[nums[i]] = i
        return None
print(two_sum([2,6,7,12],9))



                