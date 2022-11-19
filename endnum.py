t = int(input())
arr = list(map(int,input().split()))
end_arr = [0,0,0,0,0,0,0,0,0]
# count = 0
# for i in range(len(arr)):
#     b=arr[i]%10
#     # print(b)
#     for j in range(len(end_arr)):
#         # print(end_arr[j])
#         if str(end_arr[j]) in b:
#             count+=1
#         print(count)
for i in arr:
    end_arr[i%10]+=1
print(end_arr)

# for (var i of arr){
#     end_arr[i%10]+=1
    
# }
# console.log(end_arr)