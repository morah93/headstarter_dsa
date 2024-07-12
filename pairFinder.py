# In a scenario where you're given a list of unique ID badges numbers 'nums' and a security checkpoint number 'target',
# your task is to find a pair of ID badges whose numbers sum up to the security checkpoint number.
# You should return the indices of these ID badges assuming no ID badge is scanned twice and
# there exists exactly one unique pair that meets the criteria.
# The order of indices in your result does not matter.

# Example 1:
# - Input: nums = [2, 7, 11, 15], target = 9
# - Output: [0, 1]

# Example 2:
# - Input: nums = [3, 2, 4], target = 6
# - Output: [1, 2]

# Example 3:
# - Input: nums = [3,3], target = 6
# - Output: [0,1]

# Constraints:
# - The length of the list 'nums' will be at least 2 and no more than 10^4
# - Each ID badge number will be an integer in the range from -10^9 to 10^9
# - The security checkpoint number 'target' will also be an integer within the same range
# - Assure only one valid pair exists that can be scanned to match the 'target' number

def find_id_pair(nums, target):

    map = {}

    for i, value in enumerate(nums):
        complement = target - value
        if complement in map:
            return [map[complement], i]
        map[value] = i

    return []
