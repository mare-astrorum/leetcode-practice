# ORDER NESTED LIST

l = [[5,3], [3, 5], [1, 5], [8, 9], [0, 9]]
new_l = []

for i in range(len(l)):
    value = min(l)
    new_l.append(value)
    l.remove(value)

print(new_l)