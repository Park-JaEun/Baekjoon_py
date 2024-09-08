###
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
### 

N = int(input())

queen_cnt = 0
queen_pos = [False] * N        # 열에 퀸이 있는지 여부
dir41 = [False] * (2 * N) # 41대각선에 퀸이 있는지 여부
dir63 = [False] * (2 * N) # 63대각선에 퀸이 있는지 여부

def solveNQueens(row):
    global queen_cnt
    if row == N:
        queen_cnt += 1
        return
    
    for col in range(N):
        if not queen_pos[col] and not dir41[row + col] and not dir63[row - col + N]:
        # 41대각선에 있는 좌표는 행+열의 값이 동일함
        # 63대각선에 있는 좌표는 행-열의 값이 동일함
        # 음수의 가능성이 있으니 N을 더해서 양수로 만듬
            queen_pos[col] = dir41[row + col] = dir63[row - col + N] = True
            solveNQueens(row + 1)
            queen_pos[col] = dir41[row + col] = dir63[row - col + N] = False

solveNQueens(0)
print(queen_cnt)




