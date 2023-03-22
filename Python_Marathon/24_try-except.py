# value = 10/0 # ZeroDivisionError: division by zero

try:
    value = 10/0 # Couldn't catch this error anymore!
    number = int(input('Enter a number: '))
    print(number)
    # Catch the more specific error!
except ZeroDivisionError as err:
    # print('Divided by zero')
    print(err)
except ValueError:
    print('Invalid Input!')

# number = int(input('Enter a number: '))
# print(number)