count_gold = 0
count_vit = 0
count_diamond = 0
def consume_l1():
    global count_diamond, count_gold 
    count_diamond += 8
    count_gold += 1

def l1_to_l3():
    global count_gold, count_vit
    for i in range(12):
       consume_l1()
    count_gold += 0.39
    count_vit += 10

def l3_to_l4():
    global count_diamond, count_gold, count_vit
    for i in range(16):
        count_diamond += 8/0.4818
        count_gold += 1/0.4818
    count_gold += 0.897/0.4818
    count_vit += 1

def l4_to_l6():
    global count_gold, count_vit
    for i in range(12):
        l3_to_l4()
    count_gold += 19.75
    count_vit += 10

def is_suitable():
    l4_to_l6()
    count = count_gold + count_vit + count_diamond * 0.05
    if count < 750:
        print('need value is ' + str(count))
        print('自己合成是合适的')
    else:
        print('need value is' + str(count))
        print('自己合成是不合适的')

is_suitable()
