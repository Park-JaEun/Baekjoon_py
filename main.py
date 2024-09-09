###
# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1000000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
### 

import sys

# 배열을 합치기만 하는 함수
def merge(arr, low, mid, high):
    # mid를 기준으로 배열을 두 부분으로 나누고 크기 계산
    n1 = mid - low + 1
    n2 = high - mid

    # 임시 배열 L과 R에 두 부분을 저장
    L = arr[low:low + n1]
    R = arr[mid + 1:mid + 1 + n2]

    # L과 R의 첫 번째 요소부터 비교해서 arr 배열에 다시 합침
    i = 0           # L 배열의 인덱스
    j = 0           # R 배열의 인덱스
    k = low         # 병합된 배열의 시작 인덱스

  
    while i < n1 and j < n2:  # 배열을 비교하면서 작은 값을 원래 배열에 둠
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

  
    while i < n1:              # 아직 남아있는 L 배열의 요소들 추가
        arr[k] = L[i]
        i += 1
        k += 1

   
    while j < n2:                # 아직 남아있는 R 배열의 요소들 추가
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
       
        mid = low + (high - low) // 2    # 중간 지점을 계산
        
        merge_sort(arr, low, mid)        # 배열을 반으로 나누어 재귀적으로 정렬
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high       )       # 두 정렬된 부분을 병합

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])
    numbers = list(map(int, data[1:N+1]))

    merge_sort(numbers, 0, N - 1)

    sys.stdout.write("\n".join(map(str, numbers)) + "\n")
