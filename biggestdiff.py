# In this part of the session, you will be solving the following problem:
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):

# if len nums arrar is 0

# if there no val in the nums arr return 0

# find max val max func store in val

# find min val min func store in var

# find the diff between the max and min values

# return the diff
  if not len(nums):
    return 0

  max_val = max(nums)
  min_val = min(nums)

  diff = max_val - min_val
  return diff


# Step 1: Check if List is Not Empty
# Inside the biggest_diff function, first check if the list nums is not empty and has at least one element.
# This ensures that there are elements in the list to process.

# Step 2: Find Maximum Value
# If the list is not empty, use the max function to find the maximum value in the nums list.
# Store this value in the variable max_val. This will help us in calculating the difference later.

# Step 3: Find Minimum Value
# Similarly, use the min function to find the minimum value in the nums list. Store this value in the variable min_val.
# Having both the maximum and minimum values allows us to compute the difference.

# Step 4: Calculate Difference
# Calculate the difference between the max_val and min_val by subtracting min_val from max_val.
# This will give the biggest difference between any two numbers in the list.

# Step 5: Return the Difference
# Return the calculated difference. This is the final result of the function,
# representing the biggest difference between the largest and smallest values in the provided list.

# Step 6: Handle Empty List
# If the list nums is empty or not provided, return 0.
# This ensures that the function handles edge cases gracefully without errors.
