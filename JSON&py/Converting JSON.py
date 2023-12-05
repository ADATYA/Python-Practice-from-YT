# #If you have a json string you can parse it by using the json .loads() method.

# # import json

# #some JSON:
# # x='{"cname":"python","fees":3720,"duration":"2 months"}'

# #parrse x:
# # y=json.loads(x)

# #the result is Python dictionary:

# import json

# d ='{"cname":"python","fees":3720,"duration":"2 months"}'

# x = json.loads(d)

# print(type(x))
# print(x)

# for a in x:
#     print(a,x[a])

def twoSum(nums, target):
    n = len(nums)
    a = nums.copy()

    nums.sort()

    l = 0
    r = n - 1

    while l < r:
        sum = nums[l] + nums[r]

        if sum == target:
            break
        elif sum > target:
            r -= 1
        else:
            l += 1

    v = []

    for i in range(n):
        if nums[l] == a[i]:
            v.append(i)
        elif nums[r] == a[i]:
            v.append(i)

    return v