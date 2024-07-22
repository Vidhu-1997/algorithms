def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m - 1
        else:
            l = m + 1
    return -1

def main():
    print("-----------------TEST LIST(0 - 99)----------------")
    nums = [i for i in range(100)]
    target = int(input("TARGET : "))
    res = binary_search(nums, target)
    if res != -1: 
        print(res)
    else:
        print("ENTER A VALID TARGET")

if __name__ == "__main__":
    main()