# https://wikidocs.net/42528

# odd : true, even : false
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
number = input("Enter number > ")
if is_odd(int(number)):
    print("%s is odd number" % number)
else:
    print("%s is even number" % number)
