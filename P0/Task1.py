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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def get_unique_tel_nums(records):
    """
    returns set of tel. numbers made outgoing calls and received incoming calls
    """
    res = set()
    for rec in records:
        sent_num, recv_num = rec[0], rec[1]
        res.add(sent_num)
        res.add(recv_num)
    return res

count = len(get_unique_tel_nums(texts).union(get_unique_tel_nums(calls)))
print("There are {} different telephone numbers in the records.".format(count))
