# https://wikidocs.net/42527

def q_3():
    i = 1
    while i < 6:
      print("*"*i)
      i=i+1
    
def q_4():
    for i in range(1, 101):
      print(i)

def q_5():
    s_list = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
    total = 0
    for score in s_list:
        total = total + score
    print(total/len(s_list))
    
def show():
    q_3()
    q_4()
    q_5()

show()
