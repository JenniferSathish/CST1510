"""import random

def random_list(length):
    rand_list = []
    for i in range(1, length+1):
        n = random.randint(1,10)
        rand_list.append(n)
    return rand_list

r = random_list(11)
print(r)"""

"""a = [1,2,3,4,5,6,7]
sliced = a[0:3:2]
print(sliced)"""

"""a = ["watermelon", "banana", "orange", "apple", "kiwi", "kiwi"]
print(min(a))
print(max(a))
print(a.sort())
print(a.count("kiwi"))"""

L1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
L2 = []
for i in L1:
    if i%2==0:
        L2.append(i)
print(L2)

L3 = []

for i in L2:
    L3.append(L2[:5])
    print(L3)




