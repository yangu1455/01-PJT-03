# 최빈수 구하기
# 최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.

T = int(input())

for t in range(1, T+1):
    # 테스트케이스 번호 받기
    tc_num = int(input())
    # 값 받기
    case = list(map(int, input().split()))

    dict = {}
    
    for i in case:
        # 없으면 만들어 넣고
        if i not in dict:
            dict[i] = 1
        # 있으면 1을 더하고
        else:
            dict[i] += 1
    
    # dict에서 가장 큰 밸류
    # print(max(dict.values()))

    # for문 이용해서 가장 큰 밸류 값 찾고 그 밸류값을 가진 키를 리스트에 저장한다.
    # 그리고 리스트(res)에서 가장 큰 값 출력
    res = []

    for j in dict:
        if dict[j] == max(dict.values()) :
            res.append(j)

    print(f'#{tc_num} {max(res)}')