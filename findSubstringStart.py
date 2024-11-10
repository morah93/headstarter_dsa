# Imagine you have a long piece of text ('haystack') and you are looking for a specific smaller string ('needle') within it.

# Your task is to determine where in the text the smaller string first shows up.

# You should output the starting position of the first occurrence of the 'needle' in the 'haystack'.

# Should the 'needle' not be found within the 'haystack', your program must return -1, indicating its absence.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"

# Output: 0

# Explanation: The substring "sad" is first found at the start of the "haystack", thus the output is 0.

# Example 2:

# Input: haystack = "helloworld", needle = "123"

# Output: -1

# Explanation: Since "123" is not present in "helloworld", we return -1.

# Constraints:

# The length of both 'haystack' and 'needle' will be between 1 and 10^4, inclusive.

# Both 'haystack' and 'needle' will contain only lowercase English letters.

def findSubstringStart(haystack, needle):
  # if length of haystack is less than needle return -1
  if len(haystack) < len(needle):
    return -1
  # iterate thru range of haystack minus len(needle) to ensure that we have enough chars for the needle
  len_needle = len(needle)

  for i in range(len(haystack) - len_needle):
  # slice the string and check if it equals to needle
    if haystack[i: i + len_needle] == needle:
      return i
  # if needle isnt found return -1
  return -1


# Correct the calculation of len_needle to len(needle) instead of len(needle) - 1


# Update len_needle to be just len(needle) instead of len(needle) - 1


# Update line 29 to use i + len(needle) to slice haystack correctly


# Define len_needle to be equal to len(needle) on a line before using it.


# Define len_needle to be equal to len(needle) on a line before using it.


# Add 'len_needle = len(needle)' to define len_needle correctly.


# Add 'len_needle = len(needle)' after the if block to use it later in the loop.


# Add 'len_needle = len(needle)' to your code


# Consider a way to use `map` to check substrings against the needle efficiently.


# Consider creating a helper function that checks if a substring from haystack equals needle.
