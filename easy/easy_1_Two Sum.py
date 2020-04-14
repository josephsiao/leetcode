from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, element in enumerate(nums):
            try:
                another_index = nums.index(target - element, index + 1)
            except ValueError:
                another_index = None

            if (another_index is not None) and (index != another_index):
                return [index, another_index]


class Answer:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            other = target - num

            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

        return []


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        print(Solution.twoSum(nums, target))
    except Exception as e:
        print(e)
    finally:
        pass
