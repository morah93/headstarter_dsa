# Lets say that a value is "everywhere" in an array if for every pair of adjacent elements in the array, at least one of the pair is that value.
# Return true if the given value is everywhere in the array.

# isEverywhere([1, 2, 1, 3], 1) → true
# isEverywhere([1, 2, 1, 3], 2) → false
# isEverywhere([1, 2, 1, 3, 4], 1) → false

def isEverywhere(nums, val):
  # Loop through the array, but stop one element before the last one to avoid index out of range errors.
  # This is because we're checking pairs of adjacent elements.
  for i in range(len(nums) - 1):
    # Check if neither of the pair (current element and the next one) matches the value.
    # If both don't match the value, then the value is not "everywhere" according to our definition.
    if nums[i] != val and nums[i + 1] != val:
      return False  # Return False immediately if we find any pair where the value is missing.

  # If the loop completes without finding any pair missing the value, then the value is "everywhere".
  return True



# Step 1: Start Loop
# Inside the isEverywhere function, use a for loop to iterate through the list nums from the start up to the second-to-last element.
# This avoids index out of range errors since we are checking pairs of adjacent elements.

# Step 2: Check Adjacent Pairs
# Within the loop, for each iteration, check if the current element nums[i] and the next element nums[i + 1] do not match the given value val.
# If both elements in the pair are not equal to val, this means the value is not "everywhere" according to our definition.

# Step 3: Return False
# If we find any pair where both elements do not match val, return False immediately. This indicates that the given value is not "everywhere" in the array.

# Step 4: Loop Completes
# If the loop completes without finding any pair where both elements are not equal to val, return True. This signifies that the value is "everywhere" in the array.
