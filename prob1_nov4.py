tc = int(input())
num = list(map(int,input().split()))
dict = {}
n = 0
k = len(num)/2
for i in range(len(num)):
    count = 0
    for j in range(len(num)):
        if num[i]==num[j]:
            count += 1
    dict[num[i]]=count
for d in dict:
    if k>dict[d]:
        print(-1)
        break
    else:
        print(d)
        break


# for i in num:
#     if i == num[i]:
#         count+=num[i]
#         li.append[num[i]]
# if count>len(num)//2:
#     print(li[0])
# else:
#     print(-1)




# i=1
# T=int(input("enter any number="))
# list=list(map(int,input().split()))
# N=(len(list)/2) 
# k=0
# dic={}
# while k<len(list):
#     j=0
#     c=0
#     while j<len(list):
#         if list[k]==list[j]:
#             c+=1
#         j+=1
#     dic[list[k]]=c
#     k+=1
# for key in dic:
#     if N>dic[key]:
#         print(-1)
#         break
#     else:
#         print(key)
#         break
























# arr = [1,1,2,3]
# n = len(arr)
# k = 4
# x = n // k
# freq = {}
# for i in range(n):
#     if arr[i] in freq:
#         freq[arr[i]] += 1
#     else:
#         freq[arr[i]] = 1
# for i in freq:
#     if (freq[i] > x):
#         print(i)