#hackerrank question on validating a postcode

import re

# Regular expression to check if the number is in the range from 100000 to 999999
regex_integer_in_range = r'^[1-9][0-9]{5}$'

# Regular expression to check for alternating repetitive digit pairs
regex_alternating_repetitive_digit_pair = r'(\d)(\d)\1'

# Function to validate the postal code
def is_valid_postal_code(postcode):
    return (bool(re.match(regex_integer_in_range, postcode)) and
            len(re.findall(regex_alternating_repetitive_digit_pair, postcode)) < 2)

# Sample Input
postcode = '121426'

# Validate and print result
print(is_valid_postal_code(postcode))

