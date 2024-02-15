def is_full():
    return rear == size-1

def is_empty():
    return front == rear

def enQueue(item): # 꼬리를 늘려준다.
    global rear

    if is_full():
        print('queue is full')
        return

    rear += 1
    Q[rear] = item

def deQueue():
    global front

    if is_empty():
        print('queue is empty')
        return

    front += 1
    return Q[front]

def peak():
    if is_empty():
        print('queue is empty')
        return

    return Q[front+1]


size = 10
Q = [-1]*size
front = -1
rear = -1

enQueue(30)
enQueue(20)
enQueue(10)
print(Q, rear) # 꼬리의 위치를 rear에 저장
print(deQueue())
print(Q)
print(peak())