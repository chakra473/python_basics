# Python program to demonstrate
# strftime() function


from datetime import datetime as dt

# Getting current date and time
now = dt.now()
print("Without formatting", now)

# Example 1
s = now.strftime("%a %m %y")  # %a	Abbreviated weekday name,%m	Month as a zero added decimal number,
# and %y	Year without century as a zero added decimal number.
print('\nExample 1:', s)

# Example 2
s = now.strftime("%A %m %Y")  # %A	Full weekday name,%Y Year with century as a decimal number.
print('\nExample 2:', s)

# Example 3
s = now.strftime("%I %p %S")  # %-I	Hour (12-hour clock) as a decimal number,%p	Locale’s AM or PM.%S Second as a zero
# added decimal number
print('\nExample 3:', s)

# Example 4
s = now.strftime("%j")  # %j	Day of the year as a zero added decimal number.
print('\nExample 4:', s)
