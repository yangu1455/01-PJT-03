# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스는 한 개의 줄로 이루어지며, 각 줄에는 `자연수`와 `-`로 이루어진 길이가 1 이상인 문자열이 주어진다. 

# 각 테스트 케이스마다, 주어진 카드 번호로 신용 카드를 만들 수 있으면 1 만들 수 없으면 0을 출력한다.

T = int(input())

for t in range(1, T+1):
    case_b = input()
    case_a = []

    if case_b[0] not in '34569':
        print(f'#{t} 0')
        continue
    
    for b in case_b:
        if b != '-':
            case_a.append(b)
    
    if len(case_a) != 16:
        print(f'#{t} 0')
        continue
    else:
        print(f'#{t} 1')
