# https://wikidocs.net/42526

def question_01():
    displayMenu('01')
    subject = ['국어', '영어', '수학']
    score = [80, 75, 55]
    avr = 0
    
    print('과목 | 점수')
    for i in range(0, 3):
        print(subject[i], " | ", score[i])
        avr += score[i]
    
    print("평균은 ", avr/3, " 입니다.")
  
def question_02():
    displayMenu('02')
    num = 13
    if 13 % 2 == 0:
        print(num, "은 짝수입니다.")
    else:
        print(num, "은 홀수입니다.")
    
def question_03_04():
    displayMenu('03 04')
    pin = '881120-1068234'
    
    print(pin[0:6])
    print(pin[8:14])
    print(pin[7])
    
def question_05():
    displayMenu('05')
    a = "a:b:c:d"
    print(a)
    print(a.replace(":", "#"))
    
def question_06():
    displayMenu('06')
    list = [1,3,5,4,2]
    print(list)
    list.sort()
    list.reverse()
    print(list)
    
def question_07():
    displayMenu('07')
    list = ['Life', 'is', 'too', 'short']
    print(list)
    print(" ".join(list))
    
def question_08():
    displayMenu('08')
    nums = (1,2,3)
    print(nums)
    item = (4,)
    nums = nums + item
    print(nums)
    
def question_10():
    displayMenu('10')
    a = {'A': 90, 'B': 80, 'C': 70}
    print(a)
    a.pop('B')
    print(a)
    
def displayMenu(n):
    showLine(20)
    print("question ", n)
    showLine(20)
  
def showLine(n):
    print("="*n);

def start():
    question_01()
    question_02()
    question_03_04()
    question_05()
    question_06()
    question_07()
    question_08()
    question_10()
  
start()
