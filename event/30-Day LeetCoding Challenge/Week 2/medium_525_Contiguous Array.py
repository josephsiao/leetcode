from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        array_sum = 0
        sum_index_table = {0: -1}
        ans = 0
        for i in range(len(nums)):
            array_sum += 1 if nums[i] == 1 else -1
            if array_sum not in sum_index_table:
                sum_index_table[array_sum] = i
            else:
                ans = max(ans, i - sum_index_table[array_sum])

        return ans


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [0, 1]
        print(Solution.findMaxLength(nums))
    except Exception as e:
        print(e)
    finally:
        pass
