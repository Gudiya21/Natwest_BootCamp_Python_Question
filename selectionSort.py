# n =6
# def selectionSort(arr,n):
#     for i in range(0, n-1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i+1] = arr[i+1],arr[i]
#     if n>0:
#         selectionSort(arr,n-1)
# arr = [10,14,2,11,6,8]
# selectionSort(arr,n)
# print(arr) 




# def swap(a, i, j): 
#     temp = a[i]
#     a[i] = a[j]
#     a[j] = temp 
# def selectionSort(a): 
#     for i in range(len(a) - 1):
#         min = i
#         for j in range(i + 1, len(a)):
#             if a[j] < a[min]:
#                 min = j        
#         swap(a, min, i)
# a = [3, 5, 8, 4, 1, 9, -2]
# selectionSort(a)
# print(a)


def selection(arr,result):
    if len(arr) == 0:
        return ""
    else:
        j = arr.index(min(arr)) 
        arr[0],arr[j] = arr[j],arr[0]
        result.append(arr[0])
        return selection(arr[1:],result)
arr = [5,1,2,4,3]
result = [] 
selection(arr,result)
print(result)
