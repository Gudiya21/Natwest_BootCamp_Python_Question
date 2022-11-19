for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    count = 1
    res = []
    for i in range(n-1):
        if ((a[i+1]-a[i])<=2):
            count +=1 
        else:
            res.append(count)
            count = 1
    res.append(count)
    print(min(res),max(res))