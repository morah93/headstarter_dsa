# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more.
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its
# rightmost digit is less than 5, so 12 rounds down to 10.
# Given 3 ints, a b c, return the sum of their rounded values.

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
    def round10(num):
        remainder = num % 10
        if remainder >= 5:
            return num + (10 - remainder)
        else:
            return num - remainder

    return round10(a) + round10(b) + round10(c)


# Step 1: Define the Rounding Function
# Inside the round_sum function, define a helper function round10 that will handle rounding a number to the nearest multiple of 10.
# The function takes a single integer parameter num.

# Step 2: Calculate the Rightmost Digit
# Inside the round10 function, calculate the rightmost digit of num using the modulo operator: remainder = num % 10.
# This will help determine whether we need to round up or down.

# Step 3: Determine Rounding Direction
# Check if the remainder is greater than or equal to 5. If it is, we will round num up to the next multiple of 10.
# Otherwise, we will round num down to the previous multiple of 10.

# Step 4: Round Up or Down
# If the condition remainder >= 5 is true, round num up by calculating num + (10 - remainder) and return the result.
# If false, round num down by calculating num - remainder and return the result.

# Step 5: Round Each Input Number
# Back in the round_sum function, use the round10 function to round each of the input integers a, b, and c.
# This will give you the rounded values of all three numbers.

# Step 6: Sum the Rounded Values
# Calculate the sum of the three rounded values obtained from calling round10 on each input integer: round10(a) + round10(b) + round10(c).
# Return the result as the final output of the round_sum function.
