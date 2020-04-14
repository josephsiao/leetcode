class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if len(s.split()) != 0 else 0


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = "Hello World"
        print(Solution.lengthOfLastWord(x))
    except Exception as e:
        print(e)
    finally:
        pass
