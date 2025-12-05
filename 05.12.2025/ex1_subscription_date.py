from datetime import datetime, timedelta
def subscription_expiry(start_date, duration_days):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    expiry = start + timedelta(days=duration_days)
    return expiry.date()
print(subscription_expiry("2025-01-01", 40))