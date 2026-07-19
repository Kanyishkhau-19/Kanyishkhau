import random
import time

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:

        if arr[high] == arr[low]:
            comparisons += 1
            if arr[low] == target:
                return low, comparisons
            else:
                return -1, comparisons

        comparisons += 1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if pos < low or pos > high:
            break

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    print("\nPerformance Comparison")
    print("-" * 70)
    print("{:<10}{:<18}{:<18}{:<12}{:<12}".format(
        "Size", "IS Time(ms)", "BS Time(ms)", "IS Comp", "BS Comp"))
    print("-" * 70)

    sizes = [1000, 5000, 10000, 50000, 100000]

    for size in sizes:

        arr = sorted(random.sample(range(size * 10), size))
        target = random.choice(arr)

        start = time.perf_counter()

        for _ in range(100):
            idx1, comp1 = interpolation_search(arr, target)

        is_time = (time.perf_counter() - start) * 1000 / 100

        start = time.perf_counter()

        for _ in range(100):
            idx2, comp2 = binary_search(arr, target)

        bs_time = (time.perf_counter() - start) * 1000 / 100

        print("{:<10}{:<18.5f}{:<18.5f}{:<12}{:<12}".format(
            size, is_time, bs_time, comp1, comp2))

print("Interpolation Search Program")
print("-" * 35)

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter sorted elements: ").split()))

if len(arr) != n:
    print("Error: Number of elements does not match.")
    exit()

if arr != sorted(arr):
    print("Error: Array must be sorted.")
    exit()

target = int(input("Enter element to search: "))

start = time.perf_counter()
index1, comp1 = interpolation_search(arr, target)
is_time = (time.perf_counter() - start) * 1000

start = time.perf_counter()
index2, comp2 = binary_search(arr, target)
bs_time = (time.perf_counter() - start) * 1000

print("\nSearch Results")
print("-" * 35)

if index1 != -1:
    print("Interpolation Search:")
    print("Element found at index:", index1)
else:
    print("Interpolation Search:")
    print("Element not found.")

print("Comparisons :", comp1)
print("Execution Time : {:.6f} ms".format(is_time))

print()

if index2 != -1:
    print("Binary Search:")
    print("Element found at index:", index2)
else:
    print("Binary Search:")
    print("Element not found.")

print("Comparisons :", comp2)
print("Execution Time : {:.6f} ms".format(bs_time))

performance_analysis()