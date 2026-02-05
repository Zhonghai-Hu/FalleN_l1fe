# question 1
name = input("what's your name?")
print("Good afternoon " + name)

# question 2
major = input("what's your major?")
print("your major is " + major)

# question 3
city = input("What city are you from?")
print("you come from " + city)

#Part 2
#question 4
color = input("What is your favourite color? ")
food = input("What is your favourite food? ")

print("your favourite color and food is "+ color + "and " + food)

#question 5
age = input("what is your age?")
print("you are " + age + "years old")

#Part 3
#question 6
num_1 = int(input("enter one number: "))
num_2 = int(input("enter another number: "))

print("the first number is " + str(num_1) + ", and the second number is " + str(num_2))
sum = num_1 + num_2
print("the sum is " + str(sum))

#question 7
score_1 = int(input("enter one score: "))
score_2 = int(input("enter another score: "))

sum = score_1 + score_2
print("Your sum score are " + str(sum))

#part D
#question A
hour = int(input("How many hours you works."))
pay_rate = int(input("how many pay rate."))

sum = hour * pay_rate
print("total pay is " + str(sum))

#Part E
price = float(input("Enter price"))
GPA = float(input("Enter GPA"))
score = float(input("Enter score"))

price = round(price, 2)
GPA = round(GPA, 2)
score = round(score, 2)

print(f"{price:.2f}")
print(f"{GPA:.2f}")
print(f"{score:.2f}")

#Part F
## 1. input() always returns a string.

# 2. We convert input to int() or float() so we can perform calculations with numbers.

# 3. The most confusing part was figuring out when to convert user input before doing math.
