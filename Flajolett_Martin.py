import random
import math
def trailing_zeros(x):
    if x == 0:
        return 1
    count = 0
    while x & 1 == 0:
        count += 1
        x >>= 1
    return count
def evaluate_hash_function(hash_function, x):
    return eval(hash_function.replace("x", str(x)))
def flajolet_martin(dataset, hash_function, k):
    max_zeros = 0
    binary_representations = []
    trailing_zero_counts = []
    for _ in range(k):
        hash_vals = [trailing_zeros(evaluate_hash_function(hash_function, item)) for item in dataset]
        max_zeros = max(max_zeros, max(hash_vals))
        binary_representations.append([bin(evaluate_hash_function(hash_function, x))[2:].zfill(4) for x in dataset])
        trailing_zero_counts.append(hash_vals)
    estimated_distinct_count = 2 ** max_zeros
    return binary_representations, trailing_zero_counts, max_zeros, estimated_distinct_count

dataset_input = input("Enter the dataset : ")
dataset = list(map(int, dataset_input.split(',')))
hash_function = input("Enter the hash function like '(6*x + 3) % 5': ")
k = 10

binary_representations, trailing_zero_counts, max_zeros, estimated_distinct_count = flajolet_martin(dataset, hash_function, k)
print("\nBinary Conversions of Each Data Item:")
for item in dataset:
    hashed_value = evaluate_hash_function(hash_function, item)
    
print(f"Original: {item}, Hashed: {hashed_value}, Binary: {bin(hashed_value)[2:].zfill(4)}")

print("\nTrailing Zeros in Each Binary String:")
for i, item in enumerate(dataset):
    hashed_value = evaluate_hash_function(hash_function, item)
    print(f"Original: {item}, Hashed: {hashed_value}, Binary: {bin(hashed_value)[2:].zfill(4)}: {trailing_zeros(hashed_value)}")

print(f"\nMaximum Number of Trailing Zeros: {max_zeros}")
print(f"Estimated Number of Distinct Elements: {estimated_distinct_count}")
