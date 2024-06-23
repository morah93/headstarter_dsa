# Given an input string, return the number of times that the string "code" appears anywhere in the string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(s):
  count = 0
  for i in range(len(s) - 3):
      # if s[i] == 'c' and s[i + 1] == 'o' and s[i + 3] == 'e':
      if s[i:i+2] == "co" and s[i+3] == 'e':
          count += 1
  return count


# Step 1: Initialize a Count Variable
# Inside the count_code function, initialize a variable count and set it to 0.
# This variable will be used to keep track of how many times the pattern appears in the input string s.

# Step 2: Loop Through the String
# Use a for loop to iterate through the string s, starting from the beginning and stopping 4 characters before the end.
# Since we are looking for a 4-character pattern (starting with 'co' and ending with 'e'),
# we stop the loop at len(s) - 3 to avoid index out of range errors.

# Step 3: Check for Pattern Match
# Inside the loop, check if the first two characters of the current 4-character window are 'co' and
# the fourth character is 'e'. The third character can be any letter, so it is not checked specifically.

# Step 4: Increment the Count
# If the condition in the previous step is true, increment the count variable by 1.
# This indicates that the pattern 'co_e' (where _ can be any letter) has been found in the string.

# Step 5: Return the Final Count
# After the loop completes, return the final value of the count variable.
# This value represents the number of times the pattern 'co_e' appears in the input string s.
