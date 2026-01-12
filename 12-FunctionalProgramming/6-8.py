results = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

result1 = list(filter(min_pts(70), results))
result2 = list(filter(min_pts(40), results))
result3 = list(filter(min_pts(30), results))
print(result1)
print(result2)
print(result3)