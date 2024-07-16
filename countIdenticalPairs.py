# In a sequence of numbers, a pair of elements is considered 'identical' if both elements have the same value and the first element's index is less than the second element's index.
# Your task is to write a program that counts the number of such identical pairs within a given sequence of numbers, represented by an array 'nums'.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: The identical pairs are (0,3), (0,4), (3,4), and (2,5), using 0-based indexing.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Every pair in this sequence is identical.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

# Constraints:
# The length of the array 'nums' is between 1 and 100, inclusive.
# Each element in 'nums' is an integer between 1 and 100.

# Task Summary
# Step 1: Initialize the Count
# Step 2: Create a Dictionary to Store Counts
# Step 3: Iterate Over the Array
# Step 4: Check if Number Exists in Dictionary
# Step 5: Increment the Count for Good Pairs
# Step 6: Update the Dictionary
# Step 7: Return the Total Count of Good Pairs


def countIdenticalPairs(nums):
    count = 0
    num_counts = {}
    for num in range(len(nums)):
        if nums[num] in num_counts:
            count += num_counts[nums[num]]
            num_counts[nums[num]] += 1
        else:
            num_counts[nums[num]] = 1
    return count


# Step 1: Initialize the Count
# Declare a variable count and initialize it to 0. This variable will keep track of the total number of good pairs found in the array nums.

# Step 2: Create a Dictionary to Store Counts
# Initialize an empty dictionary named num_counts. This dictionary will be used to store the occurrence count of each number encountered in the array nums.

# Step 3: Iterate Over the Array
# Using a for loop, iterate over each number num in the given array nums.

# Step 4: Check if Number Exists in Dictionary
# Within the loop, check if num exists as a key in the num_counts dictionary. This check helps in identifying if the current number has been encountered before.

# Step 5: Increment the Count for Good Pairs
# If num is found in num_counts, it means a good pair is formed with each of its previous appearances.
# Increment the count by the value associated with num in num_counts. This step accounts for all the good pairs that the
# current appearance of num forms with its previous appearances.

# Step 6: Update the Dictionary
# After processing num for good pairs, update the num_counts dictionary. If num exists in the dictionary, increment its count by 1.
# If num is not in the dictionary, add it with a count of 1. This step ensures that each number’s occurrence count is accurately maintained.

# Step 7: Return the Total Count of Good Pairs
# Once all the numbers in nums have been processed, return the count. This count signifies the total number of good pairs found according to the problem's definition.
