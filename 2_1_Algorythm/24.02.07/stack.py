
# 여러 스택을 사용하여 이리 던지고 저리 던지고
def push(item, size, lst):
    if len(lst) >= size:
        print('Stack is overflow!')
    else :
        lst.append(item)

def stack_pop(lst):
    if lst:
        return lst.pop(-1)
    else:
        return f'Stack is empty!'

def top(lst):
    if lst:
        return lst[-1]
    else:
        return f'Stack is empty!'

def isempty(lst):
    if lst:
        return f'Stack is not empty!'
    else:
        return f'Stack is empty!'

stack1 = []
stack2 = []
stack3 = []
stack_size = 3
push(1,stack_size,stack1)
push(2,stack_size,stack1)
push(3,stack_size,stack1)
push(4,stack_size,stack1)
print(stack1)
print(isempty(stack2))
print(isempty(stack3))
push(stack_pop(stack1), stack_size, stack2)
print(isempty(stack2))
print(stack2)
push(stack_pop(stack1), stack_size, stack2)
push(stack_pop(stack1), stack_size, stack2)
print(stack2)
print(isempty(stack1))
push(stack_pop(stack2), stack_size, stack3)
push(stack_pop(stack2), stack_size, stack3)
push(stack_pop(stack2), stack_size, stack3)
print(stack3)
print(isempty(stack2))
print(top(stack2))
print(top(stack3))



#######################################
### Stack이라는 class를 만들어서 top은 variant, instnace method로 활용 가능하다.
def push(c):
    global top
    top += 1
    stack[top] = c

def pop():
    global top
    top -= 1
    return stack[top+1]

def is_empty():
    if top <= -1:
        print('empty')
        return 1

def peak():
    global top
    if top > -1:
        return f'top : {top}, value : {stack[top]}'
    else:
        return f'top is bottom ({top}).'

size = 10
stack = [0]*size
top = -1

push('A')
push('B')
print(stack)
print(pop())
print(stack)
print(pop())
print(is_empty())
print(peak())
push('A')
print(peak())