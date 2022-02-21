def multiplication_table(number):
    return [multiple(n, number) for n in range(1, 10)]
        # formatting
        # print("%d * %d = %d" % (number, n, n*number))
        
def multiple(x, y):
    return x*y

def displayList(number, list):
    for idx in range(len(list)):
        print("%d * %d = %d" % (number, idx+1, list[idx]))

def displayMenu():
    print("="*22)
    print("Multiplication_table")
    print("(1) All")
    print("(2) You want to number")
    print("="*22)

def start():
    displayMenu()
    
    select = input("Select Menu >>")
    
    if select == "1":
        for i in range(1, 10):
            print("-"*20)
            displayList(i, multiplication_table(i))
            
    else:
        number = int(input("Input Number >>"))
        displayList(number, multiplication_table(number))
        
start()
