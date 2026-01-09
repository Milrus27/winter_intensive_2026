#  with infinite loop practice
def safe_divide(a, b):
    try:
        a_num = float(a)
        b_num = float(b)
        c = a_num / b_num
        return f"{c}\nDivision completer successfully"
    except ZeroDivisionError:
        return 'Error: division by 0'
    except ValueError:
        return 'Error: you need to enter numbers'

while True:
    print("\n" + "="*50)
    a = input('Enter the divisible: ')
    b = input('Enter the divisor: ')
    
    result = safe_divide(a, b)
    print(result)
    
    answer = input('\nContinue dividing? (yes/no): ').lower()
    if answer != 'yes':
        print("The program is completed.")
        break