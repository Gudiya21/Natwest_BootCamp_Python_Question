# h=[3,5,0,9,8]
# i=0
# while i<len(h):
#     c=0
#     if h[i]>h[i-1]:
#         c+=1
#     print(c+1)
#     i+=1
 
# h=[3,5,0,9,8]
# i=-1
# while i>=(-len(h)):
#     print(h[i])
#     i-=1
    
    # c=0
    # if h[i]>h[i-1]:
    #     c+=1
    # print(c+1)
    # i+=1
    
# h=[3,5,0,9,8]
# i=-1
# while i>=(-len(h)):
#     c=0
#     if h[i]>h[i+1]:
#         c+=1
#     print(c+1)
#     i-=1



arr = list(map(int,input().split()))
list = []
for i in range (len(arr)-1,0,-1):
    count = 1 
    for j in range(i,-1,-1):
        if arr[i]>arr[j]:
           count = count + 1
        elif arr[i]<arr[j]:
            break
    list.append(count)
list.append(1)
print(list[::-1])