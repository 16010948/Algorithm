class Queue:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def remove(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        return self.data[0]

class Truck:
    def __init__(self, weight, position):
        self.weight = weight
        self.position = position

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = Queue()
    total = 0
    index = 0

    while True:
        answer += 1

        if index < len(truck_weights) and total + truck_weights[index] <= weight:
            bridge.add(Truck(truck_weights[index], 0))
            total += truck_weights[index]
            index += 1

        if bridge.is_empty():
            break

        flag = False
        for truck in bridge.data:
            truck.position += 1
            if truck.position >= bridge_length:
                flag = True
        if flag:
            passed_truck = bridge.remove()
            total -= passed_truck.weight

    return answer

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
# answer = 8
print(solution(bridge_length, weight, truck_weights))

bridge_length = 100
weight = 100
truck_weights = [10]
# answer = 101
print(solution(bridge_length, weight, truck_weights))

bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# answer = 110
print(solution(bridge_length, weight, truck_weights))
