scores = [
    (17,15,16,17,15),
    (16,18,19,17,19),
    (19,15,15,19,18),
    (18,17,19,15,16)
]
arr = []
for i in scores:
    row_list = list(i)
    row_list.remove(max(row_list))
    row_list.remove(min(row_list))
    arr.append(row_list)

sumy = []
for i in arr:
    sumy.append(sum(i))

print("\n".join(str(x)for x in sumy))