# In a particular email system, each email address is divided into two parts by the '@' symbol: a local part and a domain part.
# The local part may contain periods ('.') and plus signs ('+'), but these characters are processed in a special way: periods are ignored, making 'alice.bob@codeland.com' and 'alicebob@codeland.com' equivalent, and any characters following a plus sign in the local part are disregarded, so 'charlie+spam@codetown.com' is treated as 'charlie@codetown.com'.
# However, these special rules don't apply to the domain part of the email.

# Given a list of email addresses received, your task is to calculate how many unique email addresses will actually receive the email, after applying the above simplification rules to each address in the list.

# Example 1:
# Input: emails = ["test.email+yasin@theheadstarter.com","test.e.mail+faizan.ahmed@theheadstarter.com","testemail+john@the.headstarter.com"]
# Output: 2
# Explanation: After simplification, both 'test.email+yasin@theheadstarter.com' and 'test.e.mail+faizan.ahmed@theheadstarter.com' become 'testemail@theheadstarter.com', while 'testemail+john@the.headstarter.com' also remains 'testemail@theheadstarter.com', so there are 2 unique emails.

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
