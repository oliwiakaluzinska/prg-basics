import matplotlib.pyplot as plt
classification = [
    {"country":"Denmark","gold":2,"silver":4,"bronze":6},
    {"country":"Finland","gold":5,"silver":0,"bronze":4},
    {"country":"USA","gold":12,"silver":5,"bronze":11},
    {"country":"Peru","gold":0,"silver":1,"bronze":7}
]

scores = list(map(lambda x:x['gold']+x['silver']+x['bronze'], classification))
countries = list(map(lambda x:x['country'], classification))

plt.bar(countries, scores, color = 'pink')

plt.title("Olympic Games")
plt.xlabel("Countries")
plt.ylabel("Scores")

plt.show()
