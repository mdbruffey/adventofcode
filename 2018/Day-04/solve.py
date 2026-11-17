import time

def time_value(log):
    year, month, day, hour, minute = log[0]
    return minute + 60*hour + 60*24*day + 60*24*31*month + 60*24*31*12*year

def part1(logs):
    logs.sort(key=time_value)
    guards = {}
    guard_id = None
    for log in logs:
        timestamp, event = log
        if "Guard" in event:
            guard_id = int(event.split()[1].strip("#"))
        elif "falls" in event:
            start = timestamp[-1]
        elif "wakes" in event:
            end = timestamp[-1]
            if guard_id not in guards:
                guards[guard_id] = {}
            for minute in range(start, end):
                guards[guard_id][minute] = guards[guard_id].setdefault(minute, 0) + 1
        else:
            print("uhhh...")
            print(event)
    max_sleep = 0
    bad_guard = None
    for guard in guards:
        sleep = sum(guards[guard].values())
        if sleep > max_sleep:
            max_sleep = sleep
            bad_guard = guard
    common_minute = -1
    length = 0
    for minute in guards[bad_guard]:
        if guards[bad_guard][minute] > length:
            common_minute = minute
            length = guards[bad_guard][minute]
    return bad_guard*common_minute


def part2(logs):
    logs.sort(key=time_value)
    guards = {}
    guard_id = None
    for log in logs:
        timestamp, event = log
        if "Guard" in event:
            guard_id = int(event.split()[1].strip("#"))
        elif "falls" in event:
            start = timestamp[-1]
        elif "wakes" in event:
            end = timestamp[-1]
            if guard_id not in guards:
                guards[guard_id] = {}
            for minute in range(start, end):
                guards[guard_id][minute] = guards[guard_id].setdefault(minute, 0) + 1
        else:
            print("uhhh...")
            print(event)

    common_minute = -1
    frequency = 0
    bad_guard = None
    for guard in guards:
        for minute in guards[guard]:
            if guards[guard][minute] > frequency:
                common_minute = minute
                frequency = guards[guard][minute]
                bad_guard = guard
    return bad_guard*common_minute

with open("input.txt") as file:
    data = file.read().split("\n")

logs = []
for line in data:
    datetime, event = line.split("] ")
    date, timestamp = datetime.strip("[").split()
    year, month, day = list(map(int,date.split("-")))
    hour, minute = list(map(int,timestamp.split(":")))
    logs.append([(year,month,day,hour,minute), event])

start = time.perf_counter()
res1 = part1(logs)
print(f"Part 1: {res1} -- {time.perf_counter()-start:.4f} s")
start = time.perf_counter()
res2 = part2(logs)
print(f"Part 2: {res2} -- {time.perf_counter()-start:.4f} s")