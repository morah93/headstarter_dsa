# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true


def scoresClump(scores):
  for i in range(len(scores) - 2):
      if scores[i + 2] - scores[i] <= 2 and scores[i + 2] - scores[i + 1] <= 2:
          return True
  return False


# Step 1: Loop Through the Array
# Inside the scoresClump function, start a for loop that iterates through the scores array.
# Stop 2 elements before the end to avoid index out of range errors. This is because we're looking at groups of 3 adjacent scores.

# Step 2: Identify Group of Three
# In each iteration, identify a group of three adjacent scores starting from the current index i.
# The group would consist of scores[i], scores[i+1], and scores[i+2].

# Step 3: Check the Difference
# Calculate the difference between the smallest score (scores[i]) and the largest score (scores[i+2]) in
# the current group of three.  Since the array is sorted in increasing order, scores[i] is the smallest,
# and scores[i+2] is the largest in the group of three.

# Step 4: Compare the Difference
# Check if the calculated difference is less than or equal to 2.
# If it is, this means that the group of three scores differ from each other by at most 2.

# Step 5: Return True
# If a group of three scores is found where the difference is at most 2,
# return True immediately to indicate that such a group exists.

# Step 6: Loop Completion
# If the for loop completes without finding any group of three scores that differ from each other by at most 2,
# return False to indicate that such a group does not exist in the array.
