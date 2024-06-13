# In a particular email system, each email address is divided into two parts by the '@' symbol: a local part and a domain part.
# The local part may contain periods ('.') and plus signs ('+'), but these characters are processed in a special way:
# periods are ignored, making 'alice.bob@codeland.com' and 'alicebob@codeland.com' equivalent, and any characters following a plus sign in the local part are disregarded,
# so 'charlie+spam@codetown.com' is treated as 'charlie@codetown.com'.
# However, these special rules don't apply to the domain part of the email.

# Given a list of email addresses received, your task is to calculate how many unique email addresses will actually receive the email,
# after applying the above simplification rules to each address in the list.

# Example 1:
# Input: emails = ["test.email+yasin@theheadstarter.com","test.e.mail+faizan.ahmed@theheadstarter.com","testemail+john@the.headstarter.com"]
# Output: 2
# Explanation: After simplification, both 'test.email+yasin@theheadstarter.com' and 'test.e.mail+faizan.ahmed@theheadstarter.com' become 'testemail@theheadstarter.com',
# while 'testemail+john@the.headstarter.com' also remains 'testemail@theheadstarter.com', so there are 2 unique emails.

# Example 2:
# Input: emails = ["a@theheadstarter.com","b@theheadstarter.com","c@theheadstarter.com"]
# Output: 3
# Explanation: Since none of the emails use '.' or '+', all addresses are already unique.

# Constraints:
# - The list of emails will have at least 1 and no more than 100 entries.
# - Each email address will be between 1 to 100 characters long.
# - Email addresses consist of lowercase English letters, '+', '.', and '@'.
# - Each email address contains exactly one '@' character.
# - Local parts do not start with a plus character.
# - Domain names end with the '.com' suffix.

def numUniqueEmails(emails):
    pass


# Step 1: Iterate Over Each Email
# Using a for loop, iterate over each email address in the provided list of emails.
# This step is crucial for processing each email address individually according to the rules specified.

# Step 2: Split Local and Domain Parts
# For each email address, split it into two parts using the '@' symbol as a separator. This gives us two parts: the local part before '@' and the domain part after '@'.
# The split operation will result in a list with two elements: the first being the local part and the second the domain part.

# Step 3: Initialize a String for the Local Part
# Initialize an empty string x. This string will be used to accumulate characters from the local part of the email, applying rules for '.' and '+'.

# Step 4: Process Each Character in Local Part
# Iterate over each character in the local part of the email. If a character is a dot '.', skip it. If it is a plus '+', break the loop as we ignore everything after the plus.
# Otherwise, add the character to the string x which is being used to reconstruct the local part.

# Step 5: Reconstruct and Store Modified Email
# After processing the local part, concatenate x with '@' and the domain part. This results in the modified email, which follows the given rules.
# Store this modified email back in the list, replacing the original email.

# Step 6: Remove Duplicates
# Once all emails have been processed and modified according to the rules, convert the list of emails into a set.
# This operation removes all duplicate entries, since a set cannot contain duplicates.

# Step 7: Count Unique Emails
# Return the length of the set containing the modified emails. This length represents the number of unique email addresses that actually receive mails.
