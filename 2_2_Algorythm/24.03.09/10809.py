
Text = input()
order = [-1] * 26
idx = 0
for t in Text:
    if order[ord(t)-97] != -1:
        pass
    else:
        order[ord(t)-97] = idx
    idx += 1
print(*order)