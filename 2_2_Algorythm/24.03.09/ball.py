R,C = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(R)]
sumarr=[[0]*C for _ in range(R)]
memo=[[(i,j) for j in range(C)] for i in range(R)]

dr=[-1,-1,-1,0,1,1,1,0]
dc=[-1,0,1,1,1,0,-1,-1]
BIGVALUE=300005

def moveball(r,c):
    if memo[r][c]!=(r,c):
        return memo[r][c]
    
    status=False
    mmin=arr[r][c]
    nr,nc=r,c
    for i in range(8):
        nnr=dr[i]+r
        nnc=dc[i]+c
        if 0<=nnr<R and 0<=nnc<C:
            if mmin>=arr[nnr][nnc]:
                nr,nc=nnr,nnc
                mmin=arr[nr][nc]
                status=True
    if status:
        memo[r][c]=moveball(nr,nc)
    return memo[r][c]

for r in range(R):
    for c in range(C):
        nr,nc=moveball(r,c)
        sumarr[nr][nc]+=1
        
for r in range(R):
    print(*sumarr[r])