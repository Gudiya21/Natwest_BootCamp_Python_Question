def subArray(arr,s,e):
    if len(arr)==e:
        return 0
    elif s>e:
        subArray(arr,0,e+1)
    else:
        print(arr[s:e+1])
        return subArray(arr,s+1,e)
arr = [1,2,3,4]
s = 0
e = 0
subArray(arr,s,e)    