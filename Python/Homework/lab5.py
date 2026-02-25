# Name: Harrison
# Netid: ki2933
# lab 5

# questin 1
num = int(input('Enter an integer: '))

if num > 0 and num % 2 == 0:
    print('The number is positive and even.')
elif num > 0 and num % 2 == 1:
    print('The number is positive and odd.')
elif num < 0 and num % 2 == 1:
    print('The number is negative and odd.')
elif num < 0 and num % 2 == 0:
    print('The number is negative and even.')
else:
    print('The number is zero.')

# question 2
initial = int(input('Initial amount (positive number): '))
target_amount = int(input('Target amount (greater than initial amount): '))
count = 0

while initial < target_amount:
    initial = initial * 2
    print(initial)
    count += 1

print(f'It took {count} doublings to reach or exceed the target.')

# question 3
age = int(input('Enter age: '))
GPA = float(input('Enter GPA: '))
credits = int(input('Enter completed credits: '))

if GPA >= 3.0 and (age < 25 or credits >= 60):
    print('Eligible')
else:
    print('Not Eligible')

# question 4
count = 1
while count <= 50:
    if count == 37:
        break
    elif count % 6 == 0:
        count += 1
        continue
    elif count % 4 ==0 and count % 5 == 0:
        print('Special')
    else:
        print(count)
    count += 1

# question 5
total = 0
count = 0 

while True:
    num = int(input('Enter a number (0 to stop): '))
    if num == 0:
        break
    total += num
    count += 1

if count == 0:
    print("No data entered.")
else:
    print(f"Total: {total}")
    print(f"Average: {total/count:.2f}")

# question 6
for i in range(1,7):
    for x in range(1,i):
        print(x, end=" ")
    print()
