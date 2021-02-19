import re


def adjust_length(new_id):
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1] * (3 - len(new_id))
    return new_id


def cut_length(new_id):
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id


def append_a(new_id):
    if len(new_id) <= 0:
        return "a"
    else:
        return new_id


def remove_dot(new_id):
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id


def remove_double_dot(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    return new_id


def validate(new_id):
    return ''.join(re.split(r"[^a-z0-9-_.]", new_id))


def make_lower_id(new_id):
    return new_id.lower()


def solution(new_id):
    answer = ''

    answer = adjust_length(cut_length(append_a(remove_dot(remove_double_dot(validate(make_lower_id(new_id)))))))

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
# answer = "bat.y.abcdefghi"
print(solution(new_id))

new_id = "z-+.^."
# answer = "z--"
print(solution(new_id))

new_id = "=.="
# answer = "aaa"
print(solution(new_id))

new_id = 	"123_.def"
# answer = "123_.def"
print(solution(new_id))

new_id = "abcdefghijklmn.p"
# answer = "abcdefghijklmn"
print(solution(new_id))