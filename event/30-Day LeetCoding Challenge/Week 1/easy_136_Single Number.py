from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _nums = []
        for element in nums:
            if element not in _nums:
                _nums.append(element)
            else:
                _nums.remove(element)

        return _nums[0]


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [2, 2, 1]
        print(Solution.singleNumber(nums))
    except Exception as e:
        print(e)
    finally:
        pass
