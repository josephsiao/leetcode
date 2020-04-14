from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            sum_sub_array = max_sub_array = nums[0]
            for i in range(1, len(nums)):
                if sum_sub_array < 0:
                    sum_sub_array = nums[i]
                else:
                    sum_sub_array += nums[i]
                if sum_sub_array > max_sub_array:
                    max_sub_array = sum_sub_array
            return max_sub_array


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [-22, -55, 10, 8, -3, -55, 5, 6, 7, 10, -2, 10]
        print(Solution.maxSubArray(nums))
    except Exception as e:
        print(e)
    finally:
        pass
