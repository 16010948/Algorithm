string = input() + " "

result = ""
tmp = ""
is_tag = False
for char in string:
    if char == '<':
        is_tag = True

    if char == " ":
        result += tmp + char
        tmp = ""
    elif is_tag:
        tmp += char
    else:
        tmp = char + tmp

    if char == ">":
        result += tmp
        tmp = ""
        is_tag = False

print(result)