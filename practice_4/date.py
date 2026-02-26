#1 Import datetime module
from datetime import datetime, timedelta

# Get current date and time
current_date = datetime.now()

# Subtract 5 days using timedelta
five_days_ago = current_date - timedelta(days=5)


print("Current date:", current_date)
print("Date 5 days ago:", five_days_ago)


#2 from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)


print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

#3
from datetime import datetime

# Current datetime with microseconds
now = datetime.now()
print("Original datetime:", now)

# Remove microseconds
no_microseconds = now.replace(microsecond=0)
print("Datetime without microseconds:", no_microseconds)

#4
from datetime import datetime

# Example two dates
date1 = datetime(2026, 2, 25, 12, 0, 0)  # Feb 25, 2026 12:00:00
date2 = datetime(2026, 2, 24, 12, 0, 0)  # Feb 24, 2026 06:30:00

# Calculate difference
diff = date1 - date2  # Returns timedelta object

# Convert difference to total seconds
seconds = diff.total_seconds()


print("Difference in seconds:", seconds)