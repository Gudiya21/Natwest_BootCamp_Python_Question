# list=[10,14,2,11,6,8]
# for i in range(len(list)):

def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
lst = []  
for i in range(len(arr)): 
	lst.append(arr[i])	 
print(lst)



# arr = [12,4,2,6,1,8]
# n = len(arr)
# def insertion(arr,n):
#     if n>=1:
#         return 
#     insertion(arr,n-1)
#     l = arr[n-1]
    
     
# print(insertion(arr,n))

