# In the context of evaluating an inventory list represented by an array of integers, your task is to determine whether any item (number) occurs more than once.
# Your function should return true if at least one item is found in multiple instances, indicating a repeated entry in the inventory.
# Conversely, if each item is unique and no duplicates are present, your function should return false.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# The number of items in the inventory (array length) ranges from 1 to 10^5.
# Each item's identifier (integer value) can be between -10^9 and 10^9.

# Task Summary
# Step 1: Initialize a Set
# Step 2: Iterate Through the List
# Step 3: Check for Duplicates
# Step 4: Store the Element
# Step 5: Return False

def duplicate_finder(nums):
    seen = set()
    for num in nums:
        print(num)
        if num in seen:
            return True
        else:
            seen.add(num)
    return False




# Step 1: Initialize a Set
# Inside the contains_duplicate function, start by initializing an empty set named seen. This set will be used to store the unique elements from
# the nums list. Using a set is beneficial because sets cannot contain duplicate elements, and checking for the presence of an element in a
# set is done in constant time.

# Step 2: Iterate Through the List
# Use a for loop to iterate over each element in the nums list. This allows us to examine every element in the list and determine
# if it's a duplicate or not.

# Step 3: Check for Duplicates
# Within the loop, check if the current number, num, is already present in the seen set. If it is, this means that num is a duplicate
# because it appears at least twice in the list. Since we've found a duplicate, the function can return True to indicate that duplicates
# exist in the list.

# Step 4: Store the Element
# If the current number, num, is not found in the seen set, it means that this is the first time we're encountering num in the list.
# Therefore, add num to the seen set. This step ensures that we're only storing unique elements in seen,
# and if num appears again in future iterations, we'll be able to detect it as a duplicate.

# Step 5: Return False
# If the function completes iterating through the entire nums list without returning True, this means that no duplicates were found.
# Therefore, the function should return False to indicate that every element in the list is distinct.
