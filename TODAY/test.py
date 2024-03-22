

lst = [[9,3], [12,1], [10,5], [7,4], [12,4]]

lst.sort(key = lambda x: (-x[0], x[1]))
print(lst)