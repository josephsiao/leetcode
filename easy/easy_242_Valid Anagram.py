class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    try:
        Solution = Solution()
        s = "rat"
        t = "car"
        print(Solution.isAnagram(s, t))
    except Exception as e:
        print(e)
    finally:
        pass
