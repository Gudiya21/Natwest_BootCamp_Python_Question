def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        print(left)
        # mergeSort(left)
        # mergeSort(right)
        # left_index = 0
        # right_index = 0
        # position = 0
        # while left_index < len(left) and right_index < len(right):
        #     if left[left_index] < right[right_index]:
        #         arr[position] = left[left_index]
        #         left_index += 1 
        #     else:
        #         arr[position] = right[right_index]
        #         right_index += 1
        #     position+=1
        # while left_index < len(left):
        #     arr[position] = left[left_index]
        #     position += 1
        #     left_index += 1
        # while right_index < len(right):
        #     arr[position] = right[right_index]
        #     position += 1
        #     right_index += 1
        # return arr
arr = [31,2,3,55,1,66,99,100,3,12]
mergeSort(arr)
# print(arr)
    