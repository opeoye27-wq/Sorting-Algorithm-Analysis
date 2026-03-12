# Sorting Algorithm Performance Analysis

This project analyzes the performance of three classic sorting algorithms:

- Bubble Sort
- Insertion Sort
- Selection Sort

The algorithms are evaluated under several input conditions of different sizes to study how data ordering and size affects performance

## Scenarios Tested

1. Random Data
2. Sorted Data
3. Reversed Ordered Data
4. Moving 5% of elemenets from the front to the end
5. Moving 5% of elements from the end to the front

## Metrics Measured

- Number of swaps
- Execution time

## Example Results:

 Scenario     |List Size |    Bubble Sort     |   Insertion Sort   |     Selection      
------------------------------------------------------------------------------------------ 
                 |          |    Swaps, time     |    Swaps, time     |    Swaps, time     
------------------------------------------------------------------------------------------ 
     Random      |   2000   | (1001706, 0.14205) | (1001706, 0.07558) |  (1996, 0.05305)   
     Random      |   3000   | (2232781, 0.31868) | (2232781, 0.17615) |  (2993, 0.11879)

    
# Sorting-Algorithm-Analysis
Implementation and performance analysis of Bubble Sort, Insertion Sort, and Selection sort under different input scenarios
