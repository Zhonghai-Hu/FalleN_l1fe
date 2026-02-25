# Question 1
name = input("what's your name?")
age = int(input("what's your age?"))
print("Your name is " + name)
print("Your age is " + str(age))

# Question 2
num_1 = int(input("enter one number: "))
num_2 = int(input("enter another number: "))

print("the first number is " + str(num_1) + ", and the second number is " + str(num_2))
sum = num_1 + num_2
product = num_1 * num_2
diff = num_1 - num_2
print("the sum is " + str(sum))
print("the product is " + str(product))
print("the diff is " + str(diff))

# Question 3
price = float(input("The price for one item: "))
num = int(input('How many item you want to buy: '))
total_cost = price * num
print(f'The total cost is ${total_cost:.2f}')

# Part B
#Question 4
score = float(input("enter your score: "))
if score >= 60:
    print('You passed thetest.')

# Question 5
num_1 = int(input("enter one number: "))
if num_1 > 0:
    print('The numberis positive.')

#Part C
#Question 6
age = int(input("what's your age?"))
if age >= 18:
    print('ou are eligibleto vote.')
else:
    print('You are not eligibleto vote yet.')

#Question 7
num_1 = int(input("enter one number: "))
num_2 = int(input("enter another number: "))
if num_1 > num_2:
    print('The first numberis larger.')
else:
    print('The second numberis largeror they are equal.')

#Part D
#Question A
BONUS_THRESHOLD = 500
hours = int(input("How many hours you work: "))
pay_rate = float(input('Hourly pay rate: '))
total_pay = hours*pay_rate

print(f"Your total pay are {total_pay:.2f}")

if total_pay > BONUS_THRESHOLD:
    print("High earningsthis week!")

# 1. input() always returns a string

# 2. We convert input to int() or float() when we want to do math with numbers.

# 3. f-strings are useful because they make it easy to combine text and variables and format numbers.

# 4. One thing I learned about if statements is that they run code only when a condition is true.

# 5. The most confusing part of today's lab was deciding which condition to check in the if statement.

