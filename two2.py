# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
  pass


# Step 1: Initialize an Empty List
# Inside the two2 function, initialize an empty list result. This list will be used to store the numbers
# from nums after they are multiplied by 2, but only if they meet the criteria of not ending in 2.

# Step 2: Iterate Through the List
# Using a for loop, iterate through the nums list.   Get each number num for each iteration one-by-one.

# Step 3: Multiply the Number by 2
# Inside the loop, multiply the current number num by 2 and store the result in the variable doubled.

# Step 4: Check If the Number Ends in 2
# Convert the doubled number to an integer representation by checking its remainder when divided by 10.
# If doubled % 10 != 2, it means the number does not end in 2.

# Step 5: Add to the Result List
# If the number doubled does not end in 2, append it to the result list.

# Step 6: Return the Result List
# After processing all numbers in nums, return the result list,
# which contains the filtered and multiplied numbers as per the given criteria.
