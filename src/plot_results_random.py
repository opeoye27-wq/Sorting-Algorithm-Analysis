"""Graph for the random dataset"""

import matplotlib.pyplot as plt

#list sizes tested
sizes = [2000, 3000, 4000, 5000]

#Data 
bubble_times = [0.14205, 0.31868, 0.57257, 1.02597]
insertion_times = [0.07558, 0.17615, 0.30894, 0.54388]
selection_times = [0.05305, 0.11879, 0.21102, 0.39610]

plt.plot(sizes, bubble_times, label = "Bubble Sort")
plt.plot(sizes, insertion_times, label = "Insertion Sort")
plt.plot(sizes, selection_times, label = "Selection Sort")

plt.xlabel("Label Size")
plt.ylabel("Runtime (seconds)")
plt.title("Sorting Algorithm Performance (Random)")

plt.legend()

plt.savefig("graphs/random_runtime_comparisons.png")
plt.show()
