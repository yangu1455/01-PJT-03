# 1. I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. 
# s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]

# 위의 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 
# 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.

# 첫 번째 줄 : 원본 암호문의 길이 N ( 10 ≤ N ≤ 20 의 정수) N
# 두 번째 줄 : 원본 암호문 case
# 세 번째 줄 : 명령어의 개수 ( 5 ≤ N ≤ 10 의 정수) M
# 네 번째 줄 : 명령어 hey

# 위와 같은 네 줄이 한 개의 테스트 케이스이며, 총 10개의 테스트 케이스가 주어진다.

# '#' 기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개 항을 출력한다.

for t in range(1, 11):

    N = int(input())
    # 숫자 11개
    case = list(map(int, input().split()))
    M = int(input())
    # 명령어 리스트
    hey_list = list(input().split())

    for h in range(len(hey_list)):
        hey = []

        # 다음 I전까지의 숫자만으로 이뤄진 리스트 쪼개진 것
        # 명령어 1
        if hey_list[h] == 'I':
            x = int(hey_list[h+1])
            y = int(hey_list[h+2])
            
            # 숫자 y개 리스트 hey 만들기
            for i in range(h+3, h+3+y):
                hey.append(int(hey_list[i]))

            # case 리스트에서 x 전, 후를 아예 분리해서 숫자 넣고 다시 붙이자!
            f_list = []
            b_list = []
            res = []

            if x != 1:
                f_list = case[:x-1]
            else:
                f_list.append(case[0])
            b_list = case[x:] 
            
            res = f_list + hey + b_list

    print(f'#{t} {res[:10]}')


    # 아.. 지금보니까 접근이 잘못된거같다..ㅠㅠ
    # 명령을 잘라서 딕셔너리에 하나씩 넣고 빼오는게 훨씬 편할듯!