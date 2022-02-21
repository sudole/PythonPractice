# https://wikidocs.net/42528

# odd : true, even : false
def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
def q_1():   
    number = input("Enter number > ")
    if is_odd(int(number)):
        print("%s is odd number" % number)
    else:
        print("%s is even number" % number)
def q_6():
    content = input('Enter data >')
    # file
    f = open('test.txt', 'a')
    f.write(content + '\n')
    f.close()
    
def start():    
    q_1()
    q_6()
    
start()
