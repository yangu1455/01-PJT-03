# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다.

T = int(input())

for t in range(1, T+1):
    b_str = list(input())
    
    a_str = ''
    for b in b_str:
        if b == 'b':
            a_str = 'd' + a_str
        elif b == 'd':
            a_str = 'b' + a_str
        elif b == 'p':
            a_str = 'q' + a_str
        elif b == 'q':
            a_str = 'p' + a_str

    print(f'#{t} {a_str}')