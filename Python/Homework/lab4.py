# name: Harrison
# NETid: ki2933

# question 1
income = int(input('How much your income: '))
year = int(input('How many years you work: '))

if income >= 30000:
    if year >= 2:
        print('Loan Approved')
    else:
        print('Loan Denied')
else:
    print('Loan Denied')

# question 2
num = int(input('please enter a num: '))
if num >= 10 and num <= 20:
    print(num, 'is between 10 and 20')
else:
    print(num , 'is outside the range of 10 to 20')

# question 3
score = int(input('please enter the score: '))
if score < 60:
    print('your socre are',score,'and your grade is F')
elif score < 70:
    print('your socre are',score,'and your grade is D')
elif score < 80:
    print('your socre are',score,'and your grade is C')
elif score < 90:
    print('your socre are',score,'and your grade is B')
elif score <= 100:
    print('your socre are',score,'and your grade is A')
else:
    print('invalid score')

# question 4
p = input('Please enter the password: ')
password = p.lower()
if password == 'python123':
    print('Access Granted')
else:
    print('Access Denied')

# question 5
temperature = float(input('please enter today temperature: '))
rain = input('Is it raining? (yes/no)')

rain_input = rain.lower() == 'yes'
is_bad_weather = temperature < 40 or rain_input

if is_bad_weather:
    print('Stay inside.')
else:
    print('Good weather')

# question 6
score = int(input('Please enter the scores: '))
result = 'Pass' if score >= 60 else 'Fail'

print(result)

# Part 2
# question 7
loop = int(input('How many numbers you want to enter: '))
total = 0

for i in range(loop):
    num = int(input('Enter your number: '))
    total += num

print('Total total number are',total)

# question 8
score = int(input('Please enter the score: '))

while score > 100 or score < 0:
    print('error scores, please enter the score between 0 and 100')
    score = int(input('Please enter the score again: '))

print('your score is', score)

# question 9
total = 0
count = 0

while True:
    num = int(input("Enter your number (-1 to stop): "))
    
    if num == -1:
        break
    
    total += num
    count += 1

print("Total:", total)
print("Count:", count)


# question 10
for i in range(1,21):
    if i % 3 == 0:
        continue
    elif i == 17:
        break
    else:
        print(i)

# Challenge
while (value :=int(input('Enter a number: '))) < 0:
    print('Not a valid number')

print('number is',value)

# Reflection
# 1. What is the difference between and and or?
# "and" means both conditions must be True for the result to be True.
# "or" means only one condition needs to be True for the result to be True.

# 2. What is a sentinel?
# A sentinel is a special value that is used to stop a loop.

# 3. What is a Boolean variable?
# A Boolean variable is a variable that can only store True or False.

# 4. Why must loops change something inside them?
# Loops must change something inside them so the condition can eventually become False.
# Otherwise, the loop would run forever (infinite loop).

# 5. What part of today's lab was most challenging?
# The most challenging part was understanding input validation and using loops correctly.

