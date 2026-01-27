from datetime import datetime, timedelta
def count_weekdays(start_date,end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    count = 0
    while start <= end:
        if start.weekday() < 5:
            count += 1
        start += timedelta(days=1)
    return count
print(count_weekdays("2025-03-10","2025-12-5"))