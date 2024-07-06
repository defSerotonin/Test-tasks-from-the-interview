from datetime import datetime, timedelta

busy = [{'start': '10:30', 'stop': '10:50'}, {'start': '18:40', 'stop': '18:50'}, {'start': '14:40', 'stop': '15:50'},
        {'start': '16:40', 'stop': '17:20'}, {'start': '20:05', 'stop': '20:20'}]
free_time = []


def sort_list(busy_time):
    list_start = [t['start'] for t in busy_time]
    list_stop = [t['stop'] for t in busy_time]
    list_start.extend(list_stop)
    sorted_value = sorted(list_start)
    sorted_value.insert(0, '9:00')
    sorted_value.append('21:00')
    return sorted_value


sorted_list = sort_list(busy)


def time_limit(self):
    time_start = datetime.strptime(sorted_list[self], "%H:%M")
    time_stop = datetime.strptime(sorted_list[self + 1], "%H:%M")
    timer = datetime.strptime('00:30', "%H:%M")
    while time_stop >= time_start:
        memory_time = []
        memory_dict = {'start': time_start.strftime('%H:%M')}
        if time_start >= time_stop:
            break
        else:
            time_start = time_start + timedelta(hours=timer.hour, minutes=timer.minute)
            memory_dict = {'start': memory_dict['start'], 'stop': time_start.strftime('%H:%M')}
            memory_time.append(memory_dict)
            free_time.extend(memory_time)
    return


for nums in range(0, len(sorted_list), 2):
    time_limit(nums)


print(free_time)
