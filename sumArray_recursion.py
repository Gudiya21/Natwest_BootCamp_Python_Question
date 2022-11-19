def sumArray(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sumArray(arr[1:len(arr)])
print(sumArray([2,3,4,5]))
