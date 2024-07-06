# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
  pass

# Step 1: Calculate Maximum Big Bars
# Inside the make_chocolate function, calculate the maximum number of big bars that can be used without exceeding the goal.
# This is done by integer division of goal by 5 using goal // 5.   Store the result in the variable max_big_bars.

# Step 2: Determine Actual Big Bars Used
# Calculate the actual number of big bars to be used. This is the minimum value between max_big_bars and the number of big bars available (big).
# Store the result in the variable big_bars_used.

# Step 3: Calculate Remaining Weight
# Determine the remaining weight that needs to be covered after using the big bars. This is done by subtracting the total weight of the used big bars (big_bars_used * 5) from the goal.
# Store the result in the variable remaining.

# Step 4: Check Small Bars Sufficiency
# Check if the remaining weight can be covered using the available small bars. This is done by checking if remaining is less than or equal to small.
# If sufficient, return the value of remaining as the number of small bars needed.

# Step 5: Return Failure Case
# If it's not possible to cover the goal using the available bars (big and small), return -1 to indicate that it can't be done.
