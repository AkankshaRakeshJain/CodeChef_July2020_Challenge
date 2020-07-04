def sumFunction(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

for _ in range(int(input())):
    chef, morty = 0,0
    for _ in range(int(input())):
        
        a,b = map(int, input().split())
        
        if a > 9:
           a = sumFunction(a)
        if b > 9:
            b = sumFunction(b)
         
        if a < b:
            morty += 1
        elif a > b:
            chef += 1
        else:
            morty += 1
            chef += 1
    
    if chef > morty:
        print('0',chef)
    elif chef < morty:
        print('1',morty)
    elif chef == morty:
        print('2',chef)
