bottles = [508,500,512,499,492,511,503,476,501,509]

incorrectly = list(filter(lambda x: x<500*0.98 or x>500*1.02, bottles))

print((len(incorrectly)/len(bottles))*100)