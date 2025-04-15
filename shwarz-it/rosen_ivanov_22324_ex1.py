word = input().lower()

is_repeat = False
letters = []

for l in word:
    if not l in letters:
        letters.append(l)

    else:
        is_repeat = True

if not is_repeat:
    print('true')

else:
    print('false')