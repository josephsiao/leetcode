from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 10:
                return digits
            else:
                digits[i] = 0
                if (i - 1 < 0):
                    digits.insert(0, 1)
                else:
                    digits[i - 1] = digits[i - 1] + 1
        return digits


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = [9]
        print(Solution.plusOne(x))
    except Exception as e:
        print(e)
    finally:
        pass
