# Create 2 independent lists




list_1 = [1,2,3,4,5,6]
list = []
for i in range(len(list_1) - 1):
    sub = [list_1[i], list_1[i+1]]
    list.append(sub)


print (list)