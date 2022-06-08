import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    arr = sys.stdin.readline().split()
    if len(arr) == 2:
        stack.append(arr[1])
    if arr[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if arr[0] == 'size':
        print(len(stack))
    if arr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    if arr[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        
    