#dictionary comprehension finding even and odd elements
nums = [1, 2, 3, 4, 5, 6]
result = {
    "even": [x for x in nums if x % 2 == 0],
    "odd": [x for x in nums if x % 2 != 0]
}
print(result) 

#return duplicate elements in list
nums = list(map(int, input().split()))
l1 = []   # to store seen elements
l2 = []   # to store duplicates
for i in nums:
    if i in l1:
        if i not in l2:
            l2.append(i)
    else:
        l1.append(i)
print(l2)

#target equal to sum 
target = int(input())
nums = list(map(int, input().split()))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(nums[i], nums[j])