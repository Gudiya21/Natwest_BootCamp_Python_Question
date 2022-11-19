arr = [1,2,3,4,5,6]
n = 6
result = [] 
for i in range(1,2**n):
    a = str(bin(i)[2:])[::-1]
    temp = []
    for i in range(0,len(a)):
        if a[i]=='1':
            temp.append(int(arr[i]))
    result.append(temp)
print(result)
    