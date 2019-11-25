import numpy as np
import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = [] # first row -> not data

with open('Koreamedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spreadsheet")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won a gold medal")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won a silver medal")
				silvers.append(row[7])
			else: 
				print("won a bronze medal")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1
#now we can see our medal counts
print(len(golds), "gold medals")
print(len(silvers), "silver medals")
print(len(bronzes), "bronze medals")

bars1= [32, 6, 7]
bars2 = [19, 20, 3]

bars = np.add(bars1, bars2).tolist()
r = [0,1,2]
names = ['Gold','Silver','Bronze']
barWidth = 0.5

# Create brown bars
plt.bar(r, bars1, color='#cc3745', edgecolor='white', width=barWidth,label='women')
# Create green bars (middle), on top of the firs ones
plt.bar(r, bars2, bottom=bars1, color='#3b9423', edgecolor='white', width=barWidth, label='men')

plt.title("Korea Skating Medal Wins - between Wonman and Man")
plt.xticks(r, names)
plt.ylabel("Numbers")
plt.xlabel("Medal Counts Since 1992")
plt.legend()
plt.show()