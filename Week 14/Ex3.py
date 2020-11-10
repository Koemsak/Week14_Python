array = eval(input())
nbRows = len(array)
for i in range(nbRows):
    for n in array:
        if n[i] == 7:
            n[i] = 8
print(array)