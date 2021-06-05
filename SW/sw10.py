string = input()

for alpha in string:
    if alpha.isupper():
	    print(ord(alpha) - ord('A') + 1, end=" ")
    else:
        print(ord(alpha) - ord('a') + 1, end=" ")