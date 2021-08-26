"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_area_code(tel_num):
    if tel_num.startswith('(0'):
        return tel_num[:tel_num.find(')') + 1]
    if tel_num.startswith('140'):
        return '140'
    if tel_num.startswith('7') or tel_num.startswith('8') or tel_num.startswith('9'):
        return tel_num[0:4]
    return ''

def get_percentage(key, counts):
    counts_dict, total_count = counts
    return counts_dict.get(key, 0) / total_count * 100

def get_codes_called_by(code, calls):
    """
    returns tuple containing dict of called by 'code' codes with corresponding call counts
    along with total number of calls made by 'code'
    """
    code_counts = {}
    total_count = 0
    for sent_num, recv_num, _, _ in calls:
        if get_area_code(sent_num) == code:
            recv_code = get_area_code(recv_num)
            code_counts[recv_code] = code_counts.get(recv_code, 0) + 1
            total_count += 1
    return code_counts, total_count

bangalore_code = "(080)"
code_counts, total_count = get_codes_called_by(bangalore_code, calls)

print("The numbers called by people in Bangalore have codes:")
for code in sorted(code_counts.keys()):
    print(code)

print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(get_percentage(bangalore_code, (code_counts, total_count))))

