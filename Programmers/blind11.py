max_value = 0
orders_dic = {}
max_orders = []


def combination(start, order, result, n):
    global orders_dic, max_value, max_orders
    if len(result) == n:
        if result in orders_dic:
            orders_dic[result] += 1
        else:
            orders_dic[result] = 1

        if orders_dic[result] >= 2:
            if orders_dic[result] > max_value:
                max_value = orders_dic[result]
                max_orders = [result]
            elif orders_dic[result] == max_value:
                max_orders.append(result)
        return

    for i in range(start, len(order)):
        combination(i + 1, order, result + order[i], n)


def merge_sort(array):
    length = len(array)
    if length <= 1:
        return
    mid = length // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) or i2 < len(g2):
        if i2 >= len(g2) or (i1 < len(g1) and g1[i1] < g2[i2]):
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1


def solution(orders, course):
    global orders_dic, max_value, max_orders
    answer = []

    for c in course:
        max_value = 0
        orders_dic = {}
        max_orders = []
        for o in orders:
            tmp = list(o)
            merge_sort(tmp)
            combination(0, tmp, "", c)
        answer += max_orders
    merge_sort(answer)

    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))