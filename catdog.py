# In this part of the session, you will be solving the following problem:

# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(s):
    count_cat = 0
    count_dog = 0
    for i in range(len(s) - 2):
        if s[i : i + 3] == 'cat':
            count_cat += 1

        elif s[i : i + 3] == 'dog':
            count_dog += 1

    if count_cat == count_dog:
        return True
    else: return False

# Step 1: Initialize Counters
# Inside the cat_dog function, initialize two counters: count_cat and count_dog.
# Both should be set to 0 at the start. The counters will keep track of the occurrences of 'cat' and 'dog' respectively.

# Step 2: Iterate Through the String
# Using a for loop, iterate through the string s with an index i. The loop should range from 0 to len(s) - 2
# to ensure that we have at least three characters left in the string
# to check for 'cat' or 'dog'. This prevents an index out of range error.

# Step 3: Check for 'cat'
# Inside the loop, use slicing to check if the substring s[i : i + 3] is equal to 'cat'.
# If it is, increment the count_cat counter by 1.

# Step 4: Check for 'dog'
# In the same loop, use an elif statement to check if the substring s[i : i + 3] is equal to 'dog'.
# If it is, increment the count_dog counter by 1.

# Step 5: Compare Counters
# After the loop completes, compare the values of count_cat and count_dog.
# If they are equal, return True; otherwise, return False.
