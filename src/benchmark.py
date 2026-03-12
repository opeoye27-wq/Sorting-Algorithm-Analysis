import time
import random
from sorting_algorithms import bubble_sort, insertion_sort, selection_sort
from data_scenarios import move_five_percent_end, move_five_percent_front, reverse_order


list_sizes = [2000, 3000, 4000, 5000, 6000]

methods = [("Bubble Sort", bubble_sort),
            ("Insertion Sort", insertion_sort),
            ("Selection Sort", selection_sort)]

scenarios = [("Random", lambda L: L), 
             ("Sorted", sorted), 
             ("Reverse", reverse_order), 
             ("Move front to end", move_five_percent_end), 
             ("Move end to front", move_five_percent_front)]


def run_benchmark():
    for scenario_name, scenario_func in scenarios:

        for size in list_sizes:

            trial_list = [random.randint(1, 100) for i in range(size)]
            trial_list = scenario_func(trial_list)

            print(f"\nScenario: {scenario_name}  |  Size: {size}")

            for method_name, method_func in methods:

                L = trial_list.copy()
                start = time.time()
                swaps = method_func(L)
                end = time.time()
                print(f"{method_name}: swaps = {swaps}, time = {end - start: .5f}")

if __name__ == "__main__":
    run_benchmark()
