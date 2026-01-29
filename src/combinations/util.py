from itertools import combinations

def probability_of_a(n, letters, k):
    indices = [i for i in range(n) if letters[i] == 'a']

    all_combos = list(combinations(range(n), k))

    count = 0
    for combo in all_combos:
        if any(i in indices for i in combo):
            count += 1

    probability = count / len(all_combos)
    return round(probability, 4)
"""
without collections


import math

n = int(input())
letters = input().split()
k = int(input())

count_a = letters.count('a')
non_a = n - count_a

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

total = comb(n, k)

if non_a >= k:
    no_a = comb(non_a, k)
else:
    no_a = 0

probability = 1 - (no_a / total)

print(round(probability, 4))


"""