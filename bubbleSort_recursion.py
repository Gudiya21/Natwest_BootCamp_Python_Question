n =6
def bubleSort(arr,n):   
    for i in range(0, n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
    if n>0:
        bubleSort(arr,n-1)
arr = [10,14,2,11,6,8]
bubleSort(arr,n)
print(arr)