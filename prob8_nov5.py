for _ in range(int(input())):
    n,d = map(int,input().split())
    arr = list(map(int,input().split()))
    l = []
    l1 =[]
    for i in range(len(arr)):
        if arr[i]<80 and arr[i]>9:
            l.append(arr[i])
        else:
            l1.append(arr[i])
    if len(l)%d!=0:
        res = len(l)//d+1
    else: 
        res = len(l)//d 
    if len(l1)%d!=0:
        p = len(l1)//d+1 
    else:
        p = len(l1)//d
    print(res+p)
