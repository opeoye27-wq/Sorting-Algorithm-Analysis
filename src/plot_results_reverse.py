"""Graph for the reverse dataset"""

import matplotlib.pyplot as plt

#list sizes tested
sizes = [2000, 3000, 4000, 5000]

#Data 
bubble_times = [0.14357, 0.32067, 0.58241, 0.88532]
insertion_times = [0.08065, 0.18471, 0.32225, 0.49044]
selection_times = [0.05614, 0.12805, 0.23135, 0.35693]

plt.plot(sizes, bubble_times, label = "Bubble Sort")
plt.plot(sizes, insertion_times, label = "Insertion Sort")
plt.plot(sizes, selection_times, label = "Selection Sort")

plt.xlabel("Label Size")
plt.ylabel("Runtime (seconds)")
plt.title("Sorting Algorithm Performance (Reverse)")

plt.legend()

plt.savefig("graphs/reverse_runtime_comparisons.png")
plt.show()
