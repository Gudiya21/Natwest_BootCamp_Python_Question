arr = [31,19,21,35,36,9,7,1]
l = [-1]
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        l.append(arr[i-1])
    else:
        l.append(-1)
print(l)



                                            