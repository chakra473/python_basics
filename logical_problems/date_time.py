from datetime import datetime, timedelta

# Calling now() function
today = datetime.now()

print("Current date and time is", today)
# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print("initial_date", str(ini_time_for_now))

# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + timedelta(days=730)

future_date_after_2days = ini_time_for_now + timedelta(days=2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))
# Python program to demonstrate
# strftime() function


from datetime import datetime as dt

# Getting current date and time
now = dt.now()
print("Without formatting", now)

# Example 1
# s = now.strftime("%A %m %-Y")
# print('\nExample 1:', s)
#
# # Example 2
# s = now.strftime("%a %-m %y")
# print('\nExample 2:', s)
#
# # Example 3
# s = now.strftime("%-I %p %S")
# print('\nExample 3:', s)
#
# # Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)

