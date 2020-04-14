from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [1, 3, 5, 6]
        print(Solution.searchInsert(nums, 7))
    except Exception as e:
        print(e)
    finally:
        pass
