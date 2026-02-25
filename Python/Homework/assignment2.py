# Name: Harrison
# NetID: ki2933
# HW 2 Solution

# Print the program name
print('Calculate trip time')
print('-------------------')

# Get user inputs
miles = float(input('How many miles will you drive: '))
speed = float(input('How fast you drive: '))
stop = int(input('How many steps will you make: '))
time = float(input('How long is eah stop: '))

# Do a calcuation
trip_time = miles / speed * 60 + ( stop * time )

# Display the result
print('The total trip should take', trip_time, 'minutes. ')