"""Graph for the end to front dataset"""

import matplotlib.pyplot as plt

#list sizes tested
sizes = [2000, 3000, 4000, 5000, 6000]

#Data 
bubble_times = [0.14232, 0.32042, 0.56395, 0.88114, 1.28237]
insertion_times = [0.07660, 0.17306, 0.31430, 0.47656, 0.70948]
selection_times = [0.05289, 0.12001, 0.21348, 0.33103, 0.51324]

plt.plot(sizes, bubble_times, label = "Bubble Sort")
plt.plot(sizes, insertion_times, label = "Insertion Sort")
plt.plot(sizes, selection_times, label = "Selection Sort")

plt.xlabel("Label Size")
plt.ylabel("Runtime (seconds)")
plt.title("Sorting Algorithm Peroformance (End to Front))")

plt.legend()

plt.savefig("graphs/etf_runtime_comparisons.png")
plt.show()