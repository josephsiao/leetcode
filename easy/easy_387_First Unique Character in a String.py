class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}
        for i in range(len(s)):
            if s[i] in table:
                table[s[i]] = -1
            else:
                table[s[i]] = i

        for i in range(len(s)):
            if table[s[i]] != -1:
                return i

        return -1


if __name__ == "__main__":
    try:
        Solution = Solution()
        s = ""
        print(Solution.firstUniqChar(s))
    except Exception as e:
        print(e)
    finally:
        pass
