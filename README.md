# Divide and Conquer Algorithms Comparison

## Overview
This project implements and compares two popular sorting algorithms: **Merge Sort** and **Quick Sort**. The comparison is based on their performance in terms of execution time and memory usage across different types of datasets.

## Algorithms
### Merge Sort
Merge Sort is a divide-and-conquer algorithm that splits the array into halves, sorts each half, and then merges them back together. It has a time complexity of O(n log n).

### Quick Sort
Quick Sort is another divide-and-conquer algorithm that selects a pivot element and partitions the array into elements less than and greater than the pivot. It also has a time complexity of O(n log n) on average.

## Dataset Generation
The project generates various datasets for testing:
- **Sorted**: An array sorted in ascending order.
- **Reverse Sorted**: An array sorted in descending order.
- **Random**: An array filled with random integers.
- **Nearly Sorted**: An array that is mostly sorted with a few elements swapped.
- **Many Duplicates**: An array filled with a limited range of integers, resulting in many duplicate values.

## Performance Measurement
The performance of each algorithm is measured in terms of:
- **Execution Time**: Measured in milliseconds.
- **Memory Usage**: Peak memory usage during the sorting process.

## Running the Comparison
To run the comparison, execute the `divide_and_conquer_comparison.py` script. It will generate datasets of specified sizes and print the performance results for both sorting algorithms.

## Requirements
- Python 3.x
- `random`, `time`, and `tracemalloc` modules (included in the standard library)

## Conclusion
This project provides insights into the performance characteristics of Merge Sort and Quick Sort, helping to understand their efficiency in different scenarios.