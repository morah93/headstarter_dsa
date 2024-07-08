# Given an array of ints, determine if it is possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen.

# groupNoAdj(0, [2, 5, 10, 4], 12) → true
# groupNoAdj(0, [2, 5, 10, 4], 14) → false
# groupNoAdj(0, [2, 5, 10, 4], 7) → false

def groupNoAdj(start, nums, target):
    if target == 0:
        return True
    if start >= len(nums):
        return False
    if groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target):
        return True
    else: return False



# Step 1: Base Case 1 - Check if Target is Reached
# Inside the groupNoAdj function, check if the target is 0. If it is, return True as it means a valid group has been found that sums to the target.

# Step 2: Base Case 2 - Check if Start Index Exceeds Array Length
# Check if the start index is greater than or equal to the length of the nums array. If it is, return False since we've tried all elements without achieving the target sum.

# Step 3: Recursive Case - Include Current Element
# Attempt to include the current element in the group. Reduce the target by the value of the current element nums[start] and move the start pointer two positions ahead to skip the next element.
# Call groupNoAdj(start + 2, nums, target - nums[start]) to check if a valid group can be formed with this choice.

# Step 4: Check Result of Including Current Element
# If the recursive call from Step 3 returns True, return True as it means a valid group has been found using the current element.

# Step 5: Recursive Case - Skip Current Element
# Attempt to skip the current element. Move the start pointer one position ahead without changing the target.
# Call groupNoAdj(start + 1, nums, target) to check if a valid group can be formed without including the current element.

# Step 6: Check Result of Skipping Current Element
# If the recursive call from Step 5 returns True, return True as it means a valid group has been found without using the current element.

# Step 7: No Valid Group Found
# If neither including nor skipping the current element results in a valid group, return False.
# This signifies that no valid group summing to the target can be formed starting from this position considering the given constraints.
