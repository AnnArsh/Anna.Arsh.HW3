n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
min_el = lst[0]
min_el2 = lst[1]
for i in lst:
    if i < min_el:
        min_el, min_el2 = i, min_el
    elif min_el < i < min_el2:
        min_el2 = i
print('the second largest element is', min_el2)

# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# ind = 0
# for i in lst:
#     if i < min_el:
#         min_el = i
#         ind = lst.index(i)
# lst.pop(ind)
# min_el = lst[0]
# for i in lst:
#     if i < min_el:
#         min_el = i
# print(min_el)
