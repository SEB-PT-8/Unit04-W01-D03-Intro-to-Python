print('control flow lesson')

# Booleans

# && == and
# || == or
print(True and False)

# ! == not
print(not False)

# only == in python
print(5 == 5)

print(5 >= 4)


print('--------')
# if

# age = int(input('Please give your age: '))
age= 18

if age >= 18:
    print('You can drive')
elif age <18:
    print('You cannot drive')
else:
    print('Error Your age is not real')



# color = input('Enter "green", "yellow", "red": ').lower()
color='red'

if color == 'green':
    print('go')
elif color == 'yellow':
    print('slow down')
elif color == 'red':
    print('Stop')
else:
    print('Error!')




# for loops

# start at 0, go up to 5 (But NOT including 5)
for i in range(5):
    print(i)

print('--------------')

for i in range(3,10):
    print(i)

print('--------------')

for i in range(2,10,3):
    print(i)


my_students = ['Khaled','Muqtada','Sarah']

# Same as forEach() in JS
for student in my_students:
    print(student)



try:
    print('dklnlksn')
    5/0
except Exception as e:
    print('ERROR ', e)





# functions
# 1. declaring a function
def add_two_numbers(num1, num2):
    print(num1 + num2)


# 2. Calling a function
add_two_numbers(10,7)



def add_any_numbers(*args):
    print(args)
    sum = 0
    for num in args:
        sum+= num
    return sum


print(add_any_numbers(5,10,100,60,43,4,43,34,43,43))



# lambda: like arrow function for Python

def divide_two_numbers_normal(num1,num2):
    return num1/num2

#                    lambda param2, param2: function body
divide_two_numbers = lambda num1, num2: num1/num2

print(divide_two_numbers_normal(6,3))
print(divide_two_numbers(10,2))