import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())
number_list = list(map(int, str(A*B*C)))
counting_list = [0]*10

for i in range(len(number_list)):
    for j in range(10):
        if number_list[i] == j:
            counting_list[j] += 1
for i in range(10):
    print(counting_list[i])