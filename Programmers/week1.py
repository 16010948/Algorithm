def get_total_price(price, count):
    total_price = 0
    for i in range(1, count + 1):
        total_price += price * i
    return total_price


def solution(price, money, count):
    answer = -1
    total_price = get_total_price(price, count)
    answer = total_price - money if total_price > money else 0

    return answer