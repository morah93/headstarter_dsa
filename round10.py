# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more.
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10.
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
