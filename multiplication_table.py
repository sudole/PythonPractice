def multiplication_table(number):
    for n in range(1, 10):
        print(number, "*", n, "=", n*number)

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
            multiplication_table(i)
            
    else:
        number = input("Input Number >>")
        multiplication_table(int(number))
        
start()
