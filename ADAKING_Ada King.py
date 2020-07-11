# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr =[[0]*8 for i in range(8)]
    count =1
    arr[0][0]='O'
    for i in range(8):
        for j in range(8):
            if i==0 and j==0:
                continue
            if count<n:
                arr[i][j]='.'
                count+=1
            else:
                arr[i][j]='X'
    for i in range(8):
        for j in range(8):
            print(arr[i][j],end="")
        print("\n")