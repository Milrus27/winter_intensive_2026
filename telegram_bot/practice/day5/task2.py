age_inputed = input('Enter your age: ')

try:
    age = int(age_inputed)
    if age < 0:
        print('Error: age must be a positive number')
    elif age > 120:
        print('Error: too old')
    else:
        print('Great! The answer is accepted')
except ValueError:
    print('Error: you need to enter a number')