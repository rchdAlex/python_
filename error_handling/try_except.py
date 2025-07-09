user_input = input('Enter a number: ')

try:
    number = float(user_input)
    print(number)
except Exception as e:
    print(e)
    print('Sometinh went wrong...')

try:
    number = float(user_input)
    result = number / 0
    print(number)
except ValueError:
    print('Please enter a valid number!')
except ZeroDivisionError:
    print('You cannot divide by zero')
except Exception as e:
    print('error is: ', e)
