import random

def quick_sort(nums):
    if not nums: return []
    pivot = nums[-1]
    left = [i for i in nums if i < pivot]
    eq = [i for i in nums if i == pivot]
    right = [i for i in nums if i > pivot]
    return (quick_sort(left) + eq + quick_sort(right))

def main():
    print('---------------TEST RANDOM LIST---------------')
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(f"UNSORTED LIST : {nums}")
    print(f"SORTED LIST : {quick_sort(nums)}")

if __name__ == "__main__":
    main()