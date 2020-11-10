persons = eval(input())
age = int(input())
for person in (persons):
    if person[2] == age:
        print(person[0])