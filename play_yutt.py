import random
yutt_pan = {
}

my_mal = {'A': [0,0,0], 'B':[0,0,0], 'C':[0,0,0], 'D':[0,0,0]}
my_cnt = 0
your_mal = {'E':[0,0,0], 'F':[0,0,0], 'G':[0,0,0], 'H':[0,0,0]}
your_cnt = 0

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
            get_yutt_result[2] == 'back' and get_yutt_result[2] == 'back' :
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

# print(get_result)

my_cnt += 1
while my_cnt > 0 :
    my_result = move_result(make_yutt_result())
    if my_result < 4  :
        my_cnt -= 1
    else :
        my_cnt -= 1
        my_cnt += 1
    print(my_mal)
    a = input("어느 말을 고르시겠습니까?").upper()
    my_mal[a] = [0, 0, my_result]
    print(my_mal[a])


# if my_cnt > 0 :

