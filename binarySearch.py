# BinarySearch

# 1 2 3 4 5 6 7 8 9 10
# 1 2 3 4 5 | 6 7 8 9 10
# If i want to find any element in the array 
# Example I want to find 9
# So it will check
#  *9<6 or 9>6 or 9==6*

# If 9 will not find in arr than it will say that element is not in array

def binarySearch(arr,start,end,number):
    
    if start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == number:
            return mid
        elif arr[mid] > number:
            return binarySearch(arr,start,mid-1,number)
        elif arr[mid] < number:
            return binarySearch(arr,mid+1,end,number)
    else:
        return "Element is not there."
    
# Driver code 
arr = [1,2,3,4,5,6,7,8,9,10]
number = 2 
print(binarySearch(arr,0,len(arr)-1,number))

