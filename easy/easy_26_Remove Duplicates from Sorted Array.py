from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [0, 1, 1, 2, 2, 3, 3, 4]
        print(Solution.removeDuplicates(nums))
    except Exception as e:
        print(e)
    finally:
        pass
