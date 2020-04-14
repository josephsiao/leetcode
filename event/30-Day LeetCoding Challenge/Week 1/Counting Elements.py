from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr_set = set(arr)
        ans = 0
        for element in arr:
            if element + 1 in arr_set:
                ans += 1

        return ans


if __name__ == "__main__":
    try:
        Solution = Solution()
        arr = [1, 2, 3]
        print(Solution.countElements(arr))
    except Exception as e:
        print(e)
    finally:
        pass
