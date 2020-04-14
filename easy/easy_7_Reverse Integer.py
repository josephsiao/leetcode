from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x <= -2**31:
            return 0

        if x < 0:
            y = int(str(x)[0] + str(x)[len(str(x)):0:-1])
        else:
            y = int(str(x)[::-1])

        return 0 if (y > 2**31-1 or y <= -2**31) else y


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = 47412
        print(Solution.reverse(x))
    except Exception as e:
        print(e)
    finally:
        pass
