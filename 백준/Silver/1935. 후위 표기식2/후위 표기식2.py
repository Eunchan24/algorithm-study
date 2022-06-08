# 피연산자 만나면 push, 연산자 만나면 pop

N = int(input())
sen = input()
alpha = [0] * N 

for i in range(N):
    alpha[i] = int(input()) # 피연산자에 대응하는 값 받기

stack = [] # 스택 선언

for i in sen:
    if 'A' <= i <='Z': # 피연산자이면 
        stack.append(alpha[ord(i)- ord('A')]) # 숫자로 스택에 저장
    else: # 연산자이면
        str2 = stack.pop()
        str1 = stack.pop()
        
        if i == '+':
            stack.append(str1 + str2)
        elif i == '-':
            stack.append(str1 - str2)
        elif i == '*':
            stack.append(str1 * str2)
        elif i == '/':
            stack.append(str1 / str2)

print('%.2f' %stack[0])