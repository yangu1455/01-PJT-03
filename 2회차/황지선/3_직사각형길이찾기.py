# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 
# 세 자연수 a, b, c(1 ≤ a, b, c ≤ 100)가 공백으로 구분되어 주어진다.
# 각 테스트 케이스마다 나머지 한 변의 길이를 출력한다.

T = int(input())

for t in range(1, T+1):
    a, b, c = map(int, input().split())
    dict = {}

    # 딕셔너리에 넣어서 밸류가 1 아님 3인 경우의 키 값을 얻어오면 됨.
    for i in [a, b, c]:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    d = 0
    for j in dict:
        if dict[j] % 2 == 1:
            d = j
            
    print(f'#{t} {d}')