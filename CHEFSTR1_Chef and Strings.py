for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split())) 
    sum = 0

    for i in range(len(s)-1):
        diff = s[i] - s[i+1]
        if diff < 0:
            diff = -(diff)
        sum+= diff-1

    print(sum)


# 1
# 6
# 1 6 11 6 10 11