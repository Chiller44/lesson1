import random

nums1 = []
nums2 = []
nums3 = []
for i in range(20):
    nums1.append(random.randint(-35, 35))
for y in range(15):
    nums2.append(random.randint(-35, 35))
print('Список 1: ', nums1)
print('Список 2: ', nums2)
for i in nums1 and nums2:
    if i in nums1 and nums2:
        nums3.append(i)
print('Елементи обох списків: ', nums3)
z = nums1 + nums2
c = []
for i in z:
    if i not in c:
        c.append(i)
print('Елементи обох списків: ', c)
m = []
for i in nums1:
    if i == max(nums1):
        m.append(i)
        if max(nums1) == max(nums1):
            break
print(m)

