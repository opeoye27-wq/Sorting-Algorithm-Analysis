"""Graph for the move front to end dataset"""

import matplotlib.pyplot as plt

#list sizes tested
sizes = [2000, 3000, 4000, 5000]

#Data 
bubble_times = [0.13931, 0.31634, 0.56037, 0.88606]
insertion_times = [0.07607, 0.17493, 0.29949, 0.49326]
selection_times = [0.05322, 0.11980, 0.21421, 0.33147]

plt.plot(sizes, bubble_times, label = "Bubble Sort")
plt.plot(sizes, insertion_times, label = "Insertion Sort")
plt.plot(sizes, selection_times, label = "Selection Sort")

plt.xlabel("Label Size")
plt.ylabel("Runtime (seconds)")
plt.title("Sorting Algorithm Peroformance (Move Front to End)")

plt.legend()

plt.savefig("graphs/fte_runtime_comparisons.png")
plt.show()