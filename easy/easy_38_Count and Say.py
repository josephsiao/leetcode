import re


class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = 4
        print(Solution.countAndSay(nums))
    except Exception as e:
        print(e)
    finally:
        pass
