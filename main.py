###
### 

def isPrime(NUM):
    for num in range(2, NUM):
        if(NUM % num) == 0:
            return False
    return True

N = int(input())
numbers = []
for n in range(N):
    numbers.append(int(input()))

for num in numbers:
    for count in range(num//2):
        if isPrime(num//2- count):
           if isPrime(num - (num//2- count)):
            print(num//2- count, num - (num//2- count))
            break
