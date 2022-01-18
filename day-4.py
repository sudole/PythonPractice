import math

def formatTest():
    # Formatted string literals
    print(f'The value of pi is approximately {math.pi :.3f}.')

    # The String format() Method
    print('The value of pi is approximately {}'.format(math.pi))

    # Old string formatting
    print('The value of pi is approximately %5.3f.' % math.pi)


# Exception, Error

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause\n")

# Success
divide(2, 1)

# Exception
divide(2, 0)

divide("2", "1")