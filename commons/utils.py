from datetime import datetime, timedelta

def days_range(num_days=30):
    now = datetime.now()
    delta = timedelta(days=num_days)
    return now - delta