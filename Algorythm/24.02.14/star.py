import sys
sys.stdout = open('star_output.txt', 'w')

N = int(input())
for i in range(2*N-1):
    if i <= N-1:
        print(f'{" "*(N-(i+1))}{"*"*(2*(i+1)-1)}')
    else:
        print(f'{" "*(i-N+1)}{"*"*(2*(2*N-1-i)-1)}')