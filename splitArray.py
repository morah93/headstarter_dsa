# Given an array of ints, return a boolean to determine if it is possible to divide the ints into two groups, so that the sums of the two groups are the same.
# Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray().

# splitArray([2, 2]) → true
# splitArray([2, 3]) → false
# splitArray([5, 2, 3]) → true

def splitArray(nums):
  def split_array_helper(nums, i , sum1, sum2):
    if i == len(nums):
      return sum1 == sum2
    return split_array_helper(nums, i + 1, sum1 + nums[i], sum2) or split_array_helper(nums, i + 1, sum1, sum2 + nums[i])
  return split_array_helper(nums, 0, 0, 0)

# Step 1: Define the Helper Function
# Inside the splitArray function, define a helper function named splitArrayHelper. This function will handle the recursive process of dividing the array into two groups.

# Step 2: Base Case of the Recursion
# Inside the splitArrayHelper function, define the base case.   If the index has reached the length of nums, this means we have considered all elements.
# In this case, return whether sum1 is equal to sum2.

# Step 3: Recursive Call for Group 1
# Inside the splitArrayHelper function, make the first recursive call to try adding the current element to group 1.
# Call splitArrayHelper with the index incremented by 1, and update sum1 to include the current element nums[index].

# Step 4: Recursive Call for Group 2
# Inside the splitArrayHelper function, make the second recursive call to try adding the current element to group 2.
# Call splitArrayHelper with the index incremented by 1, and update sum2 to include the current element nums[index].

# Step 5: Combine Results from Recursive Calls
# Inside the splitArrayHelper function, return the logical OR (using the or operator) of the results from both recursive calls.
# This checks if either adding the current element to group 1 or to group 2 results in equal sums.

# Step 6: Initial Call to Helper Function
# In the main splitArray function, make the initial call to splitArrayHelper with index set to 0 and both sum1 and sum2 set to 0.
# This starts the recursive process from the beginning of the array.
