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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def get_unique_tel_nums(records):
    """
    returns tuple containing set of tel. numbers made outgoing calls and set of tel. numbers received incoming calls
    """
    sent = set()
    recv = set()
    for rec in records:
        sent_num, recv_num = rec[0], rec[1]
        sent.add(sent_num)
        recv.add(recv_num)
    return sent, recv

def get_possible_telemarketers_list(texts, calls):
    texts_sent, texts_recv = get_unique_tel_nums(texts)
    calls_sent, calls_recv = get_unique_tel_nums(calls)
    return sorted(list(calls_sent.difference(calls_recv.union(texts_sent.union(texts_recv)))))

print("These numbers could be telemarketers: ")
for num in get_possible_telemarketers_list(texts, calls):
    print(num)
