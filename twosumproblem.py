## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
##Example 1:

#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(nums,target):
    # Create a hash map to store the numbers we've seen
    num_map ={}
    # Loop through the array
    for index,num in enumerate(nums):
        diff = target-num # Calculate the difference we need
        if diff in num_map: # Check if the difference is in the map
            return [num_map[diff],index] # Return the two indices
        num_map[num] =index # Add the current number to the map
s=two_sum([2,7,11,15],9)
print(s)