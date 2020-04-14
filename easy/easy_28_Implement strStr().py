class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:len(needle) + i] == needle:
                return i

        return -1


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = ''
        print(Solution.strStr(x, ''))
    except Exception as e:
        print(e)
    finally:
        pass
