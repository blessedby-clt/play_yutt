import random

mal = {'A': [0,0,0], 'B':[0,0,0], 'C':[0,0,0], 'D':[0,0,0], 'a':[0,0,0], 'b':[0,0,0], 'c':[0,0,0], 'd':[0,0,0]}
## ABCD : 내 말, abcd : 적말
my_turn = 1 ## 1 : 내 턴, 0 : 적턴
my_cnt = 0
mal_select = 1
test = 0
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

def move_result(number) :
    if number == 0 :
        return 5
    else :
        return number

# while my_mal['A'][0] = 1 or my_mal['B'][0] = 1 or my_mal['C'][0] = 1 or my_mal['D'][0] = 1 :
while mal['A'][0] + mal['B'][0] + mal['C'][0] + mal['D'][0] < 4  and mal['a'][0] + mal['b'][0] + mal['c'][0] + mal['d'][0] < 4:
    my_cnt += 1
    while my_cnt > 0 :
        if my_turn == 1 :
            print("########내 턴######")
        else :
            print("########적 턴######")

        my_result = move_result(make_yutt_result())
        print(my_result)
        print(mal)
        if my_result < 4  :
            my_cnt -= 1
        print("남은 윷 던지는 횟수:", my_cnt)
        ### 말 고르는 선택지
        while mal_select > 0 :
            a = input("어느 말을 고르시겠습니까?")
            # 엉뚱한 말을 고른 경우, 선택이 불가능하도록.
            try :
                if my_turn == 1:
                    a = a.upper()
                else :
                    a = a.lower()
            except :
                print("해당 말은 선택할 수 없습니다")

            if my_result == -1 and mal[a] == [0, 0, 0]:
                mal[a] = [0, 0, 19]
                mal_select = 0
            elif my_result == -1 and mal[a] == [0, 0, 1]:
                mal[a] = [1, 0, 0]
                mal_select = 0
            elif mal[a][0] > 0:
                print("해당 말은 선택할 수 없습니다")
            elif mal[a] == [0,0,0] :
                mal[a][2] += my_result
                mal_select = 0
            else :
                if my_turn == 1 :
                    for idx in 'ABCD' :
                        if idx == a :
                            pass
                        elif idx != a and mal[a] == mal[idx] :
                            mal[idx][2] += my_result
                        else :
                            pass
                    mal[a][2] += my_result
                else :
                    for idx in 'abcd' :
                        if idx == a :
                            pass
                        elif idx != a and mal[a] == mal[idx] :
                            mal[idx][2] += my_result
                        else :
                            pass
                    mal[a][2] += my_result
                mal_select = 0
        mal_select = 1

        if mal[a] == [0, 0, 5]:
            b = input("방향을 바꾸겠습니까?(Y/N)").upper()
            if b == 'Y':
                if my_turn == 1:
                    for idx in 'ABCD':
                        if a == idx :
                            pass
                        elif a != idx and mal[a] == mal[idx] :
                            mal[idx][1] = 1
                            mal[idx][2] = 0
                    mal[a][1] = 1
                    mal[a][2] = 0
                else :
                    for idx in 'abcd':
                        if a == idx :
                            pass
                        elif a != idx and mal[a] == mal[idx] :
                            mal[idx][1] = 1
                            mal[idx][2] = 0
                    mal[a][1] = 1
                    mal[a][2] = 0


        elif mal[a] == [0, 0, 10]:
            b = input("방향을 바꾸겠습니까?(Y/N)").upper()
            if b == 'Y':
                if my_turn == 1:
                    for idx in 'ABCD':
                        if a == idx:
                            pass
                        elif a != idx and mal[a] == mal[idx]:
                            mal[idx][1] = 2
                            mal[idx][2] = 0
                    mal[a][1] = 2
                    mal[a][2] = 0
                else:
                    for idx in 'abcd':
                        if a == idx:
                            pass
                        elif a != idx and mal[a] == mal[idx]:
                            mal[idx][1] = 2
                            mal[idx][2] = 0
                        mal[a][1] = 2
                        mal[a][2] = 0

        elif mal[a] == [0,1,3] :
            b = input("방향을 바꾸겠습니까?(Y/N)").upper()
            if my_turn == 1:
                for idx in 'ABCD':
                    if a == idx:
                        pass
                    elif a != idx and mal[a] == mal[idx]:
                        mal[idx][1] = 2
                        mal[idx][2] = 3
                mal[a][1] = 2
                mal[a][2] = 3
            else:
                for idx in 'abcd':
                    if a == idx:
                        pass
                    elif a != idx and mal[a] == mal[idx]:
                        mal[idx][1] = 2
                        mal[idx][2] = 3
                    mal[a][1] = 2
                    mal[a][2] = 3

        elif mal[a] == [0,2,3] :
            b = input("방향을 바꾸겠습니까?(Y/N)").upper()
            if my_turn == 1:
                for idx in 'ABCD':
                    if a == idx:
                        pass
                    elif a != idx and mal[a] == mal[idx]:
                        mal[a][1] = 1
                        mal[a][2] = 3
                mal[a][1] = 1
                mal[a][2] = 3
            else:
                for idx in 'abcd':
                    if a == idx:
                        pass
                    elif a != idx and mal[a] == mal[idx]:
                        mal[a][1] = 1
                        mal[a][2] = 3
                    mal[a][1] = 1
                    mal[a][2] = 3

        elif mal[a][1] == 1 and mal[a][2] > 5 :
            if my_turn == 1:
                for idx in 'ABCD':
                    mal[idx][1] = 0
                    mal[idx][2] = mal[idx][2]+9
            else :
                for idx in 'abcd':
                    mal[idx][1] = 0
                    mal[idx][2] = mal[idx][2]+9


        print(my_cnt)
        print(mal[a])
        ## 말 이동 후 적 말을 잡을 수 있는지
        if my_turn == 1 :
            for idx in 'abcd' :
                if mal[a] == mal[idx] :
                    print(mal[idx])
                    mal[idx] = [0,0,0]
                    test += 1
            if test > 0 :
                my_cnt += 1
            test = 0

        else :
            for idx in 'ABCD':
                if mal[a] == mal[idx] :
                    mal[idx] = [0, 0, 0]
                    test += 1
            if test > 0 :
                my_cnt += 1
            test = 0

        if my_turn == 1:
            for idx in 'ABCD' :
                if mal[idx][1] == 0 and mal[idx][2] >= 20 | mal[idx][1] > 0 and mal[idx][2] > 5 :
                    mal[idx][0] = 1
                else :
                    pass
        else :
            for idx in 'abcd' :
                if mal[idx][1] == 0 and mal[idx][2] >= 20 | mal[idx][1] > 0 and mal[idx][2] > 5 :
                    mal[idx][0] = 1
                else :
                    pass

    if my_turn == 1 :
        my_turn = 0
    else :
        my_turn = 1


