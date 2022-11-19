for _ in range(int(input())):
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        count = 0
        for j in arr:
            if j==arr[i]:
                count+=1 
        if count==1:
            print(arr[i])
 

 