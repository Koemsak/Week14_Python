def isEqual(list1, list2):
    isEqual = True
    if len(list1) == len(list2):
        for i in range(len(list1)):
            value1 = list1[i]
            value2 = list2[i]
            isEqual = isEqual and (value1 == value2)
    else:
        isEqual = False
    return isEqual
list1 = eval(input())
list2 = eval(input())
if isEqual(list1, list2):
    print("EQUAL")
else:
    print("NOT EQUAL")