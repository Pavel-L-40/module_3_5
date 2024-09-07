def get_multiplied_didgits(num):
    str_num = str(num)
    if len(str_num) == 1:
        return int(str_num)
    first = int(str_num[0])
    if first == 0:
        first = 1
    num = str_num[1:]
    return first * get_multiplied_didgits(num)

num = int(input())
res = get_multiplied_didgits(num)
print(res)
