import random

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    left = merge_sort(nums[:m])
    right = merge_sort(nums[m:])
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    merged = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    return merged

def main():
    print('---------------TEST RANDOM LIST---------------')
    nums = [random.randint(1, 1000) for _ in range(10)]
    print(f"UNSORTED LIST : {nums}")
    print(f"SORTED LIST : {merge_sort(nums)}")

if __name__ == "__main__":
    main()