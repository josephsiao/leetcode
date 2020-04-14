from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_table = {}
        for _, element in enumerate(nums):
            if element in nums_table:
                return True
            else:
                nums_table[element] = 1

        return False


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [1, 2, 3, 1]
        print(Solution.containsDuplicate(nums))
    except Exception as e:
        print(e)
    finally:
        pass
