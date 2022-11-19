# def bubbleSort(array):
#   for i in range(len(array)):
#     for j in range(0, len(array) - i - 1):
#       if array[j] > array[j + 1]:
#         temp = array[j]
#         array[j] = array[j+1]
#         array[j+1] = temp       
# data = [-2, 45, 0, 11, -9]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)

# list=[10,14,2,11,6,8]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list):
#         if list[i]<list[j]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
#         j+=1
#     i+=1
# print(list)
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