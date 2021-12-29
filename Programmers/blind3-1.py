def combination(menu, idx, order, n, menus):
    menu = ''.join(sorted(menu))
    if idx == len(order):
        if len(menu) == n:
            if menu in menus:
                menus[menu] += 1
            else:
                menus[menu] = 1
            return menus[menu]
        return 0

    max_order = 0
    if len(menu) < n:
        max_order = max(max_order, combination(menu + order[idx], idx + 1, order, n, menus))
    max_order = max(max_order, combination(menu, idx + 1, order, n, menus))

    return max_order


def solution(orders, course):
    answer = []

    for n in course:
        menus = {}
        max_order = 0
        for order in orders:
            max_order = max(max_order, combination('', 0, order, n, menus))

        if max_order >= 2:
            for menu in menus:
                if menus[menu] == max_order:
                    answer.append(menu)
    answer.sort()

    return answer