import random
yutt_pan = {
}

my_mal = {1:0, 2:0, 3:0, 4:0}
your_mal = {5:0, 6:0, 7:0, 8:0}

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

get_result = make_yutt_result()

# if get_result == 0 or get_result == 5 :
# else :
#

print(get_result)