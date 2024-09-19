arr = [1,4,7,-5,9,3]
d = dict()
target = 4
ans = []
for i in range(len(arr)):
    if target-arr[i] in d:
        ans.append([i,d[target-arr[i]]])
    d[arr[i]] = i #d{1:0, 4:1}

print(ans)