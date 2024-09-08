###
# 하노이탑
### 

def hanoi(N, start, end, temp):
    if N == 1:
        print(start, end)
    else:
        hanoi(N-1,start, temp, end)
        print(start, end)
        hanoi(N-1,temp, end, start)


N = int(input())

print(pow(2,N)-1)

if N <= 20:
    hanoi(N, 1,3,2)





