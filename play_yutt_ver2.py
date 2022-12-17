### 의사코드 작성
# 내팀을 정의
# 상대팀을 정의
# 조작자 = 내팀
# ## ABCD : 내 말, abcd : 적말
# my_turn = 1 ## 1 : 내 턴, 0 : 적턴
# chance_cnt = 0
# mal_choice_cnt = 1
# while 게임 종료 조건 불만족 :
#     조작기회 = 1
#     while 조작자 기회 > 0 :
#         윷을 던진다
#         조작기회 차감
#         if 윷, 모? :
#             기회 += 1
#             바로 말을 고르지 않고 윷을 던질 수 있음 (일단 여기서는 고려하지 않기로 함... -> 어려움)
#         말 선택
#         if 이미 도착한 말?
#             선택 불가능
#         업을 수 있는 말 체크
#         if 내 위치가 방향 이동이 가능한가? :
#             방향 이동 여부 결정
#             업힌 말도 같이이동해야 함
#         말 이동
#         if 빽도 :
#             if 시작점 :
#                 완주 조건에서 1칸 모자라게 이동시킴
#         else :
#              이동
#         if 이동한 위치에서 상대말 잡을 수 있는지 검사 :
#             상대말 위치 리셋
#             기회 추가
#         완료 여부 체크

#         if 만약 조작자가 A면
#             조작자 = B
#         else:
#             조작자 = A
import random

class Team() :
    def __init__(self, team_name, mal_list):
        self.team_name = team_name
        self.mal_list = mal_list

def dice_yutt() :
    ## 평평한 면이 앞면
    yutt_result = {}
    for i in range(4) :
        if random.random() >= 0.5 :
            yutt_result[i] = 'front'
        else :
            yutt_result[i] = 'back'

    return yutt_result

def make_yutt_result() :
    get_yutt_result = dice_yutt()
    print(get_yutt_result)
    result = 0
    # 0번째 idx의 윷을 빽도가 있는 특수윷으로 간주
    if get_yutt_result[0] == 'front' and get_yutt_result[1] == 'back' and   \
            get_yutt_result[2] == 'back' and get_yutt_result[3] == 'back' :
        result = -1
    else :
        ## result = 0으로 유지되는 경우는 모.
        for i, j in get_yutt_result.items() :
            if j == 'front' :
                result += 1
    return result

def interpret_yutt_result(result) :
    yutt_info = {1:'도', 2:'개', 3:'걸', 4:'윷', 5:'모', -1 :'빽도'}
    return yutt_info[result]

def move_result(number) :
    if number == 0 :
        return 5
    else :
        return number

## 윷을 엎을 수 있는지 체크
def check_move_together(mal_name) :
    count_result = ''
    for mal_idx in player.mal_list :
        if mal[mal_idx] == mal[mal_name] :
            count_result += mal_idx
    return count_result

## 방향 전환이 가능한지 체크
def check_direction(mal_list) :
    if mal[mal_list[0]] in ([0, 0, 5], [0, 0, 10], [0, 1, 3], [0, 2, 3]):
        return True
    else :
        return False

## 말을 잡을 수 있는지 체크
def check_chase_opp_mal() :
    chase_opp_mal_list = ''
    for mal_idx in opp.mal_list :
        if mal[mal_name] == mal[mal_idx] :
            chase_opp_mal_list += mal_idx
        elif mal[mal_name][1:] == [1,3] and mal[mal_idx][1:3] == [2,3] :
            chase_opp_mal_list += mal_idx
        elif mal[mal_name][1] == 0 and mal[mal_name][2] >=15 and mal[mal_idx][1] == 1 and mal[mal_idx][2] >= 6:
            if mal[mal_name][2] == mal[mal_idx][2]+9 :
                chase_opp_mal_list += mal_idx
        elif mal[mal_name][1] == 1 and mal[mal_name][2] >= 6 and mal[mal_idx][1] == 0 and mal[mal_idx][2] >= 15:
            if mal[mal_name][2] == mal[mal_idx][2] - 9 :
                chase_opp_mal_list += mal_idx
    return chase_opp_mal_list

## 도착 여부 체크
def check_complete(mal_list) :
    for idx in mal_list :
        if mal[idx][1] == 0 and mal[idx][2] >= 20:
            return True
        elif mal[idx][1] == 2 and mal[idx][2] >= 6:
            return True
        elif mal[idx][1] == 1 and mal[idx][2] >= 11:
            return True



mal = {'A': [0,0,0], 'B':[0,0,0], 'C':[0,0,0], 'D':[0,0,0], 'a':[0,0,0], 'b':[0,0,0], 'c':[0,0,0], 'd':[0,0,0]}

my = Team('my', 'ABCD')
your = Team('your', 'abcd')
player = my
opp = your

while mal['A'][0] + mal['B'][0] + mal['C'][0] + mal['D'][0] < 4  and mal['a'][0] + mal['b'][0] + mal['c'][0] + mal['d'][0] < 4:
    chance_cnt = 1
    print("#####", player.team_name, "차례 #####")

    while chance_cnt > 0 :
        mal_choice_cnt = 1

        my_result = move_result(make_yutt_result())
        print("결과 :", interpret_yutt_result(my_result))

        chance_cnt -= 1

        if my_result >= 4 :
            chance_cnt += 1
            print("윷 또는 모가 나왔습니다!")
        while mal_choice_cnt > 0 :
            mal_name = input("말을 선택해주세요.")
            if player.team_name == 'my' :
                mal_name = mal_name.upper()
            else :
                mal_name = mal_name.lower()

            if mal_name in player.mal_list :
                if mal[mal_name][0] > 0 :
                    print("말을 다시 선택해주세요.")
                else :
                    mal_choice_cnt -= 1
            else :
                print("말을 다시 선택해주세요.")

        if mal[mal_name] != [0,0,0] :
            move_mal_list = check_move_together(mal_name)
        else :
            move_mal_list = mal_name
        print(move_mal_list)

        if check_direction(move_mal_list) :
            direction_question = input("방향을 바꾸시겠습니까?(Y/N)").upper()
            if direction_question == 'Y':
                temp_mal_name = move_mal_list[0]
                print(temp_mal_name)
                if mal[temp_mal_name][1:] == [0,5] :
                    for idx in move_mal_list :
                        mal[idx] = [0, 1,0]
                        print(mal[idx])
                elif mal[temp_mal_name][1:] == [0,10] :
                    for idx in move_mal_list:
                        mal[idx] = [0,2,0]
                        print(mal[idx])
                elif mal[temp_mal_name][1:] == [1,3] :
                    for idx in move_mal_list :
                        mal[idx] = [0, 2,3]
                        print(mal[idx])
                elif mal[temp_mal_name][1:] == [2,3] :
                    for idx in move_mal_list:
                        mal[idx][1:2] = [1,3]
                        print(mal[idx])

        if my_result == -1 :
            if mal[mal_name] == [0,0,0] :
                for idx in move_mal_list :
                    mal[idx] = [0, 0, 19]
            elif mal[mal_name] == [0,0,1] :
                for idx in move_mal_list :
                    mal[idx] = [0, 0, 20]
            else :
                for idx in move_mal_list:
                    mal[idx][2] += my_result
        else :
            for idx in move_mal_list:
                mal[idx][2] += my_result


        check_chase_mal = check_chase_opp_mal()

        if len(check_chase_mal) > 0 :
            for mal_idx in check_chase_mal :
                mal[mal_idx] = [0,0,0]
            chance_cnt += 1
            print("말을 잡았습니다.")
        print(mal)
        print("남은횟수 :",chance_cnt)

    if check_complete(move_mal_list) == True :
        for idx in move_mal_list :
            mal[idx][0] = 1

    if player == my :
        player = your
        opp = my
    else :
        player = my
        opp = your

print("#####", opp.team_name, ": 승리 #####" )

### To-do list
# 1. 주석 달아놓기
# 2. 윷/모가 뜬 상태에서는 바로 말을 옮기지 않고 윷을 한 번 더 던진 후에 말을 옮기는 것 구현
# 3. 말을 옮길 수 있는 횟수가 남아도, 승리 조건 만족하면 break로 빠져나오게 만들기
# 4. 말을 파악하기가 어려움 -> 적어도 말판 위에 말을 매칭시키는 것 필요

# while 게임이 끝?
#     조자작의 기회 = 1
#     while 조자작의 기회 > 0
#       윷을 던진다
#       어떤말을 보낼지 결정한다.
#       if 선택한 말이 모퉁이에 있나?
#          어디로 갈지 선택한다
#       if 결과가 윷이나 모면
#        기회 += 1
#       결과에 따라서 어떻게 이동시킬지 입력을 받는다.
#       이동시킨다.
#       if 이동시켰는데 다른 말을 잡은 경우
#          기회 +=1
#          잡은 말 원점으로 보내기
#       else if 내 말을 업은 경우
#          말을 업힌다
#     if 만약 조작자가 A면
#         조작자 = B
#     else:
#         조작자 = A