from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(1, len(nums)):
            if nums[i] != 0 and nums[ptr] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
            if nums[ptr] != 0:
                ptr += 1
        return nums


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [1, 0, 1]
        print(Solution.moveZeroes(nums))
    except Exception as e:
        print(e)
    finally:
        pass
