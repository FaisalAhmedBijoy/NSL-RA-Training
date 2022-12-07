"""
A valid credit card from ABCD Bank has the following characteristics:

► It must start with 4 ,5  or 6 .
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4  or more consecutive repeated digits.

Sample Input

6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456
Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid
"""
import re
number_of_test_cases = int(input())
for _ in range(number_of_test_cases):
    credit_card_number = input()
    # first check [456] then three digit [0-9]{3} then three digit [0-9]{4} then three digit [0-9]{4} then three digit [0-9]{4} then end of string $
    test1 = re.fullmatch(r'^[456][0-9]{3}(-?[0-9]{4}){3}$', credit_card_number)
    # consecutive check  <re.Match object; span=(2, 6), match='3333'> otherwise None
    test2 = re.search(r'([0-9])\1\1\1', credit_card_number.replace('-', ''))
    # print(test2)
    if test1 and not test2:
        print('Valid')
    else:
        print('Invalid')