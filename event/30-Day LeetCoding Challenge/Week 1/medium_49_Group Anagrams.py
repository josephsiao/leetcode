from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


if __name__ == "__main__":
    try:
        Solution = Solution()
        strs = ["eat", "tea", "tan", "ate", "nat", "bat", "google", "ooggle"]
        print(Solution.groupAnagrams(strs))
    except Exception as e:
        print(e)
    finally:
        pass
