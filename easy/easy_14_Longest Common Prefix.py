from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            else:
                result.append(i[0])

        return ''.join(result)


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = ["flower", "flow", "flight"]
        print(Solution.longestCommonPrefix(x))
    except Exception as e:
        print(e)
    finally:
        pass
