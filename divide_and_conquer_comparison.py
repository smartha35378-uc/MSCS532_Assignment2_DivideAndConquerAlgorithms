import random
import time
import tracemalloc

# ---------------- Merge Sort ----------------
def merge_sort(arr):
    # If list has 0 or 1 item, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):
    # Store sorted values here
    result = []
    i = j = 0

    # Compare values from both lists
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining values
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------- Quick Sort ----------------
def quick_sort(arr):
    # If list has 0 or 1 item, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose middle value as pivot
    pivot = arr[len(arr) // 2]

    # Divide values into three groups
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Sort left and right and join all parts
    return quick_sort(left) + middle + quick_sort(right)


# ---------------- Create datasets ----------------
def generate_datasets(n):
    # Create random data
    base = [random.randint(1, 100000) for _ in range(n)]

    # Nearly sorted: swap a few elements
    nearly_sorted = sorted(base)
    for i in range(int(n * 0.05)):  # swap 5% of elements
        idx1 = random.randint(0, n - 1)
        idx2 = random.randint(0, n - 1)
        nearly_sorted[idx1], nearly_sorted[idx2] = nearly_sorted[idx2], nearly_sorted[idx1]

    # Many duplicates
    duplicates = [random.randint(1, 10) for _ in range(n)]

    return {
        "Sorted": sorted(base),
        "Reverse Sorted": sorted(base, reverse=True),
        "Random": base,
        "Nearly Sorted": nearly_sorted,
        "Many Duplicates": duplicates
    }


# ---------------- Measure time and memory ----------------
def measure(algorithm, data):
    # Start memory tracking
    tracemalloc.start()

    # Start time
    start = time.perf_counter()

    # Run sorting algorithm
    algorithm(data.copy())

    # End time
    end = time.perf_counter()

    # Get memory used
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    # Convert time to milliseconds
    time_ms = (end - start) * 1000

    return time_ms, peak


# ---------------- Run comparison ----------------
def run_comparison(sizes=(1000, 5000)):
    for n in sizes:
        print(f"\nDataset size: {n}")

        # Create all dataset types
        datasets = generate_datasets(n)

        for dtype, data in datasets.items():
            # Measure Merge Sort
            time_merge, memory_merge = measure(merge_sort, data)

            # Measure Quick Sort
            time_quick, memory_quick = measure(quick_sort, data)

            # Print results
            print(f"\n{dtype} data:")
            print(f"Merge Sort  - Time: {time_merge:.3f} ms | Memory: {memory_merge} bytes")
            print(f"Quick Sort  - Time: {time_quick:.3f} ms | Memory: {memory_quick} bytes")


# ---------------- Main program ----------------
if __name__ == "__main__":
    run_comparison()
