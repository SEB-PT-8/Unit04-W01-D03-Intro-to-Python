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
except:
    print('ERROR')