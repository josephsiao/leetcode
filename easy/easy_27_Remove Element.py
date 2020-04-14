from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)

        return len(nums)


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [3, 2, 2, 3]
        print(Solution.removeElement(nums, 3))
    except Exception as e:
        print(e)
    finally:
        pass
