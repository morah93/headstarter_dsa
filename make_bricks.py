# We want to make a row of bricks that is goal inches long.
# We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks.

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
  max_big_bricks = goal // 5
  remaining_goal = goal - (max_big_bricks * 5)
  print(remaining_goal)
  if remaining_goal <= small:
    return True
  return False

# Step 1: Initialize Variables
# Inside the make_bricks function, we start by defining a variable max_big_bricks.
# This will store the maximum number of big bricks (each 5 inches long) that can be used without exceeding the goal.

# Step 2: Calculate Max Big Bricks
# Set max_big_bricks to the smaller value between the number of big bricks available (big) and
# the maximum number of big bricks needed to get close to the goal (```goal // 5").

# Step 3: Calculate Remaining Goal
# Calculate the remaining inches we need to cover after using the maximum number of big bricks.
# Store this value in the remaining_goal variable. We do this by subtracting the inches covered by big bricks,
# calculated as max_big_bricks * 5, from the goal.

# Step 4: Check Small Bricks Availability
# Check if the number of small bricks (each 1 inch long) is enough to cover the remaining_goal.
# If the number of small bricks (small) is greater than or equal to the remaining_goal,
# it means we can achieve the goal using the available bricks.

# Step 5: Return Result
# Return True if the condition in Step 4 is met. Otherwise, return False.
