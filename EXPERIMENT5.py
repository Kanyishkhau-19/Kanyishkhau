import random
import time

comparisons = 0

def min_max_dc(arr, low, high):
    global comparisons
    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparisons += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    min1, max1 = min_max_dc(arr, low, mid)
    min2, max2 = min_max_dc(arr, mid + 1, high)

    comparisons += 2

    minimum = min1 if min1 < min2 else min2
    maximum = max1 if max1 > max2 else max2

    return minimum, maximum

def min_max_naive(arr):

    comparisons = 0

    minimum = maximum = arr[0]

    for i in range(1, len(arr)):

        comparisons += 1
        if arr[i] < minimum:
            minimum = arr[i]

        comparisons += 1
        if arr[i] > maximum:
            maximum = arr[i]

    return minimum, maximum, comparisons
def performance_test():

    print("\nPerformance Comparison")
    print("-" * 75)

    print("{:<10}{:<12}{:<12}{:<18}{:<18}".format(
        "Size",
        "DC Comp",
        "Naive",
        "DC Time(ms)",
        "Naive Time(ms)"
    ))

    print("-" * 75)

    sizes = [10, 100, 1000, 5000, 10000]

    global comparisons

    for size in sizes:

        arr = random.sample(range(size * 10), size)

        comparisons = 0

        start = time.perf_counter()

        min_max_dc(arr, 0, len(arr) - 1)

        dc_time = (time.perf_counter() - start) * 1000

        dc_comp = comparisons

        start = time.perf_counter()

        _, _, naive_comp = min_max_naive(arr)

        naive_time = (time.perf_counter() - start) * 1000

        print("{:<10}{:<12}{:<12}{:<18.6f}{:<18.6f}".format(
            size,
            dc_comp,
            naive_comp,
            dc_time,
            naive_time
        ))

print("=" * 60)
print("DIVIDE AND CONQUER - MINIMUM & MAXIMUM")
print("=" * 60)

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter elements: ").split()))

if len(arr) != n:
    print("Error! Number of elements doesn't match.")
    exit()

comparisons = 0

start = time.perf_counter()

minimum, maximum = min_max_dc(arr, 0, len(arr) - 1)

dc_time = (time.perf_counter() - start) * 1000

dc_comp = comparisons


start = time.perf_counter()

nmin, nmax, naive_comp = min_max_naive(arr)

naive_time = (time.perf_counter() - start) * 1000


print("\nResults")
print("-" * 40)

print("Minimum Element :", minimum)
print("Maximum Element :", maximum)

print("\nDivide & Conquer")
print("Comparisons :", dc_comp)
print("Execution Time : {:.6f} ms".format(dc_time))

print("\nNaive Method")
print("Comparisons :", naive_comp)
print("Execution Time : {:.6f} ms".format(naive_time))
formula = (3 * n) // 2 - 2 if n > 1 else 0

print("\nTheoretical Comparisons (3n/2 - 2):", formula)

performance_test()