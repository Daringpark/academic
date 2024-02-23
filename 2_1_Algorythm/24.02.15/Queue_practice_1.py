# 4개의 데이터를 차례대로 큐에 삽입하고 차례대로 꺼내서 출력하시오.
# FIFO (First In, First Out)
numbers = [1,2,3,4]
queue1 = []

for i in range(4):
    queue1.append(numbers[i])
    print(queue1)

for i in range(4):
    print(queue1.pop(0), end = ' ')

queue1.append(numbers[0])
queue1.append(numbers[1])
queue1.append(numbers[2])
queue1.pop(0)
queue1.append(numbers[3])
N = int(input())
order = (N-1)%len(queue1) # (N-1)%list_length = 시작을 1로 보는 경우 # 순서 0 ~ N-1
print(queue1)
print(queue1[order])