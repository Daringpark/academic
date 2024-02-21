
# # Global-local arguments practice 1

# A = 0
# n = int(input())

# def func() : 
#     global A # 주석처리를 하게 된다면, local variable을 함수 내에서 정의해줘야한다.
#     # 기존 global variable을 쓸꺼면 재정의를 해주자.

#     for i in range(n) :
#         if A > 16 :
#             A -= 1
#         else :
#             A += 4
        
#     result = A
#     return result

# print(func())
    
# Global-local arguments practice 2

a = 32
b = 64
c = 128
d = 256

def world() :
    a = 64
    print(a,b,c,d) #64, 64, 128, 256

    def village1(c, d) :
        c = 64
        d = 128
        print(a,b,c,d)

    def village2(b) :
        b = 32
        print(a,b,c,d)

    def village3(a, c) :
        print(a,b,c,d)

    village1(32, 128) #64, 64, 64, 128
    print(a,b,c,d) #64, 64, 128, 256

    village2(16) #64, 32, 128, 256
    print(a,b,c,d) #64, 64, 128, 256

    village3(256, 512) #256, 64, 512, 256

world()
