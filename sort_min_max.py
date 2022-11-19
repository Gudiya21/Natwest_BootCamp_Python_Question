n = list(map(int,input().split()))
s = set(n)
l = list(s)
l.sort()
if len(l)<3:
    print("Not Possible")
else:
    print(l[0:3])
    print(l[-3::])



# print()

# n=[1,2,3]
# sub_array=[]
# for i in range(0,len(n)):
#     for j in range(i,len(n)):
#         sub_array.append(n[i:j])
# print(sub_array)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    











# arr = list(map(int,input().split()))
# n = len(arr)
# arr = sorted(arr)
# l=list(arr) 
# check = 0
# count = 1
# for i in range(1, n + 1):
#     if(count < 4):
#         if(check != l[n - i]):
#             print(l[n - i], end = " ")
#             check = l[n - i]
#             count += 1
#     else:
#         break



