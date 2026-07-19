import time

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons

def compute_lps(pattern):
    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length != 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                matches.append(i - j)
                j = lps[j - 1]

        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, q=101):

    d = 256
    n = len(text)
    m = len(pattern)

    h = pow(d, m - 1, q)

    p_hash = 0
    t_hash = 0

    comparisons = 0
    matches = []

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    for i in range(n - m + 1):

        if p_hash == t_hash:

            for j in range(m):
                comparisons += 1

                if text[i + j] != pattern[j]:
                    break
            else:
                matches.append(i)

        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


print("=" * 60)
print("STRING MATCHING ALGORITHMS")
print("=" * 60)

text = input("Enter Text    : ")
pattern = input("Enter Pattern : ")

print()

start = time.perf_counter()

naive_match, naive_comp = naive_search(text, pattern)

naive_time = (time.perf_counter() - start) * 1000


start = time.perf_counter()

kmp_match, kmp_comp = kmp_search(text, pattern)

kmp_time = (time.perf_counter() - start) * 1000


start = time.perf_counter()

rk_match, rk_comp = rabin_karp(text, pattern)

rk_time = (time.perf_counter() - start) * 1000


print("=" * 70)
print("{:<15}{:<20}{:<15}{:<15}".format(
    "Algorithm", "Match Positions", "Comparisons", "Time(ms)"))
print("=" * 70)

print("{:<15}{:<20}{:<15}{:<15.6f}".format(
    "Naive", str(naive_match), naive_comp, naive_time))

print("{:<15}{:<20}{:<15}{:<15.6f}".format(
    "KMP", str(kmp_match), kmp_comp, kmp_time))

print("{:<15}{:<20}{:<15}{:<15.6f}".format(
    "Rabin-Karp", str(rk_match), rk_comp, rk_time))

print("=" * 70)


times = {
    "Naive": naive_time,
    "KMP": kmp_time,
    "Rabin-Karp": rk_time
}

fastest = min(times, key=times.get)

print("\nFastest Algorithm :", fastest)