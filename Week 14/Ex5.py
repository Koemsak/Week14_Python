array = eval(input())
nbRows = len(array)
nbCol = len(array[0])
result = []
for index in range(nbCol):
    sum = 0
    for row in range(nbRows):
        sum += array[row][index]
    result.append(sum)
print(result)