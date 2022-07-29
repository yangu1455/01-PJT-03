# 당신은, n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력해야 한다.

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 이후 T개의 테스트 케이스에 대해 각각 두 줄로 주어진다.
# 첫 번째 줄에는 정수의 개수 N 이 주어지며(1 ≤ N ≤ 10,000), 
# 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다. 
# 이 정수들은 각각 1 이상 100,000 이하이다.

# 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
# 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

T = int(input())

for t in range(1, T+1):
    tc_num = int(input())
    case = list(map(int, input().split()))

    # 키 = 소득, 밸류 = 해당 소득 사람 수
    people = {}
    for c in case:
        if c not in people:
            people[c] = 1
        else:
            people[c] += 1
    
    # 평균을 구한다.
    py = sum(case) / len(case)

    # 평균 이하인 키 값을 가진 사람들의 수(밸류)를 전부 더한다.
    hap = 0
    for j in people:
        if j <= py:
            hap += people[j]

    # 출력한다.
    print(f'#{t} {hap}')