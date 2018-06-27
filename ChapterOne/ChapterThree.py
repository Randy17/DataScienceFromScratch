from matplotlib import pyplot as plt
from collections import Counter

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 545.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color = 'green', marker = 'o', linestyle = 'solid')

plt.title('Номинальный ВВП')

plt.ylabel('Млрд. $')
plt.show()

#Bar chart------------------------------
movies = ['Anny Hall', 'Ben-Gur', 'Casablanka', 'Handi', 'Westside story']
num_oscars = [5, 11, 3, 8, 10]

xs = [i + 0.5 for i, _ in enumerate(movies)]

plt.bar(xs, num_oscars)
plt.ylabel('Oscars count')
plt.title('My favorive movies')

plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()

#Histogram-----------------------------
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade : grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()],
        histogram.values(),
        8)

plt.axis([-5, 105, 0, 5]) # X - (-5, 105); Y - (0, 5)

plt.xticks([10 * i for i in range(11)])
plt.xlabel('Decile')
plt.ylabel('Students count')
plt.title('Grades ')
plt.show()

#------------------------------
variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

total_error = [x + y for x, y in zip(variance, bias_squared)]

xs = [i for i, _ in enumerate(variance)]

plt.plot(xs, variance, 'g-', label = 'variance')
plt.plot(xs, bias_squared, 'r-', label = 'bias squared')
plt.plot(xs, total_error, 'b:', label = 'total error')

plt.legend(loc=9)
plt.xlabel('Model complexity')
plt.title('Variance and bias squared')
plt.show()

#scatterplot----------------
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy = (friend_count, minute_count),
                 xytext=(5, -5),
                 textcoords='offset points')
plt.title('Friends - minutes dependency')
plt.xlabel('Friends count')
plt.ylabel('minutes')
plt.show()

