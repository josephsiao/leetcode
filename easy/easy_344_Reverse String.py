from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) < 2:
            return s

        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

        return s


if __name__ == "__main__":
    try:
        Solution = Solution()
        s = ["h", "e", "l", "l", "o"]
        print(Solution.reverseString(s))
    except Exception as e:
        print(e)
    finally:
        pass
