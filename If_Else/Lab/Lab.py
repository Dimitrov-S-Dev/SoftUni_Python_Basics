# # Task 1 Excellent Grade
# grade = float(input())
#
# if grade >= 5.50:
#     print("Excellent")
#
# # Task 2 Higher Number
#
# first = int(input())
# second = int(input())
#
# if first > second:
#     print(first)
# else:
#     print(second)
#
# # Task 3 Odd Even Number
#
# num = int(input())
#
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")
#
# # Task 4 Guess password
#
# correct_pass = "s3cr3t!P@ssw0rd"
# user_guess = input()
#
# if user_guess == correct_pass:
#     print("Welcome")
# else:
#     print("Wrong password")
#
#
# # Task 5 Numbers from 100 to 200
#
# num = int(input())
#
# if num < 100:
#     print("Less than 100")
# elif num > 200:
#     print("Greater than 200")
# else:
#     print("Between 100 and 200")
#
#
# # Task 6 Speed Info
#
# speed = float(input())
#
# if speed <= 10:
#     print("slow")
# elif speed <= 50:
#     print("average")
# elif speed <= 150:
#     print("fast")
# elif speed <= 1000:
#     print("ultra fast")
# else:
#     print("extremely fast")
import math

# Task 7 Shapes Areas

shape = input()
a = None
b = None
result = None

if shape == "square":
    a = float(input())
    result = a * a
elif shape == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
elif shape == "circle":
    a = float(input())
    result = a ** 2 * math.pi
elif shape == "triangle":
    a = float(input())
    b = float(input())
    result = (a * b) / 2

print(f"{result:.3f}")


