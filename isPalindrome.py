# Consider the challenge of identifying whether a given sequence of characters forms a palindrome, specifically after adjusting its format.
# This involves firstly rendering all capital letters to their lowercase equivalents and secondly, discarding any characters that are neither part of the alphabet nor numerals.
# Should the adjusted sequence mirror itself when reversed, it is recognized as a palindrome.

# Given a string `s`, devise a function that determines whether this string qualifies as a palindrome under the conditions mentioned, returning `true` if it does, and `false` if otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: Following adjustments, "amanaplanacanalpanama" presents a mirrored sequence.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: Post-adjustment, "raceacar" fails to exhibit symmetry.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: Once non-alphanumeric characters are removed, `s` becomes an empty string "", which inherently meets the criteria of a palindrome.

# Constraints:
# - The string `s` length will range from 1 to 200,000 characters.
# - `s` will only comprise printable ASCII characters.

def isPalindrome(s):
  # normalise string by iterating thru s and removing all non alphanum chars and making it lowercase
  new_S = "".join(char.lower() for char in s if char.isalnum())
  # return true or false if new_S == the reversed new_S
  return new_S == new_S[:: -1]
