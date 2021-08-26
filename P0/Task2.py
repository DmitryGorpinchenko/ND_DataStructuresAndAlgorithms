"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def get_most_busy_tel_num(calls):
    """
    returns tuple containing tel. number spent the longest time on the phone
    along with the time spent in seconds
    """
    busy_times = {}
    for sent_num, recv_num, _, dur in calls:
        busy_times[sent_num] = busy_times.get(sent_num, 0) + int(dur)
        busy_times[recv_num] = busy_times.get(recv_num, 0) + int(dur)

    most_busy_num = max(busy_times, key = lambda k: busy_times[k])
    max_time = busy_times.get(most_busy_num)

    return most_busy_num, max_time

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(*get_most_busy_tel_num(calls)))

