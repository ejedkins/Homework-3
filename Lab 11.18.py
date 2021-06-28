#Elijah Jedkins PSID: 1786452
nums = input()
num_list = nums.split()

list=[]

for i in num_list:
    i = int(i)
    if i >= 0:
        list.append(i)
list.sort()
for i in list:
    print(i, end=' ')