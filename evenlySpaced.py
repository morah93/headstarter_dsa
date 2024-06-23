# Given three ints, a b c, one of them is small, one is medium and one is large.
# Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.

# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

def evenlySpaced(a, b, c):
  val = (a, b, c)
  x = sorted(val)
  diff1 = x[0] - x[1]
  diff2 = x[1] - x[2]
  if diff1 == diff2:
    return True
  else: return False


# Step 1: Sort the Numbers
# Inside the evenlySpaced function, use the sorted function to sort the input numbers a, b, and c in ascending order.
# The sorted list will help us easily identify which numbers are small, medium, and large.

# Step 2: Calculate First Difference
# After sorting the numbers, calculate the difference between the first and second numbers in the sorted list.
# This difference, which we'll call diff1, represents the difference between the small and medium numbers.

# Step 3: Calculate Second Difference
# Next, calculate the difference between the second and third numbers in the sorted list.
# This difference, which we'll call diff2, represents the difference between the medium and large numbers.

# Step 4: Compare the Differences
# Compare diff1 and diff2.   If they are equal, it means the numbers are evenly spaced.
# If they are not equal, the numbers are not evenly spaced.

# Step 5: Return the Result
# Return the result of the comparison. Specifically, if diff1 == diff2, return True; otherwise, return False.
# This completes the function's logic.
