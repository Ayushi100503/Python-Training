from datetime import datetime
def count_mondays(timestamps):
    count = 0
    for ts in timestamps:
        dt = datetime.strptime(ts, '%Y-%m-%d')

        if dt.weekday() == 0:
            count += 1
    return count

print(count_mondays(["2025-01-06", "2025-01-07", "2025-01-13"]))