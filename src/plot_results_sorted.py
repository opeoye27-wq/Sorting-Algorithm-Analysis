"""Graph for the sorted dataset"""

import matplotlib.pyplot as plt

#list sizes tested
sizes = [2000, 3000, 4000, 5000]

#Data 
bubble_times = [0.00007, 0.00011, 0.00014, 0.00018]
insertion_times = [0.00016, 0.00024, 0.00032, 0.00042]
selection_times = [0.06019, 0.13445, 0.23591, 0.37004]

plt.plot(sizes, bubble_times, label = "Bubble Sort")
plt.plot(sizes, insertion_times, label = "Insertion Sort")
plt.plot(sizes, selection_times, label = "Selection Sort")

plt.xlabel("Label Size")
plt.ylabel("Runtime (seconds)")
plt.title("Sorting Algorithm Peroformance (Sorted)")

plt.legend()

plt.savefig("graphs/sorted_runtime_comparisons.png")
plt.show()