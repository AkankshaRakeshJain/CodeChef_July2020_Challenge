def check(lst):
    count = {}
    for i in lst:
        count[i] = count.get(i,0) + 1
    return count

for _ in range(int(input())):
    n = int(input())
    A_lst=[]
    for _ in range(4*n-1):
        A_lst.append(list(map(int, input().split())))
    B_lst,C_lst = [],[]

    for i in A_lst:
        B_lst.append(i[0])
        C_lst.append(i[1])

    D = check(B_lst)
    E = check(C_lst)
    
    for i,j in D.items():
        if j%2!=0:
            F = i
    for i,j in E.items():
        if j%2!=0:
            G = i

    print(F,G)

    