# In this part of the session, you will be solving the following problem:
# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8).
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):
  pass





# Step 1: Initialize Variables
# Inside the sum78 function, initialize total_sum to 0 and in_section to False. These variables will be used to store the sum of the valid numbers and to flag whether
# we are currently in a section starting with a 7 and ending with an 8, respectively.

# Step 2: Iterate Through the List
# Using a for loop, iterate through the nums list. In each iteration, the variable num will represent the current element in the list.

# Step 3: Check for the Start of a Section
# Inside the loop, check if the current number num is 7. If it is, set the in_section flag to True to start ignoring numbers until we find an 8.

# Step 4: Check for the End of a Section
# If the current number num is 8 and the in_section flag is True, set the in_section flag to False to end the section and start adding numbers to the sum again.

# Step 5: Add Number to Sum
# If we are not in a section (i.e., in_section is False), add the current number num to total_sum.
# This ensures that only numbers outside of the 7-8 sections are included in the sum.

# Step 6: Return the Sum
# After the loop finishes iterating over the entire list, return the total_sum, which now contains the sum of all valid numbers that are not in any 7-8 sections.
