num = list(map(int,input().split()))
n = int(input())
sum = 0
for i in range(n):
    for j in num:
        sum+=j
if sum>9:
    sum_ten = 0
    while sum>0:
        mod = sum%10
        sum_ten+=mod
        sum//=10
    print(sum_ten)
else:
    print(sum)