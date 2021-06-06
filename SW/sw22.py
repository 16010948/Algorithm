T = int(input())

for test_case in range(1, T + 1):
    string = input()
    classification = {}
    for alpha in string:
        if alpha in classification:
            classification[alpha] += 1
        else:
            classification[alpha] = 1
    result = "Yes"
    for key in classification:
        if classification[key] != 2:
            result = "No"

    print("#" + str(test_case), result)