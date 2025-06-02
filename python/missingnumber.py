def missingNumber(nums):
    n = len(nums)
    xor_all = 0
    xor_nums = 0

    for i in range(n + 1):
        xor_all ^= i
    for num in nums:
        xor_nums ^= num

    return xor_all ^ xor_nums

# Example usage:
if __name__ == "__main__":
    nums = [3, 0, 1 , 4 , 2 ,6]
    print("The missing number is:", missingNumber(nums))  # Output: 2
