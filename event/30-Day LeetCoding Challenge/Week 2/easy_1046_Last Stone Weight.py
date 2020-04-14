from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def smash(x: int, y: int):
            if x == y:
                return None
            else:
                return abs(x - y)

        while len(stones) > 1:
            stones.sort()
            res = smash(stones.pop(), stones.pop())
            if res:
                stones.append(res)

        return stones[0] if stones else 0


if __name__ == "__main__":
    try:
        Solution = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        print(Solution.lastStoneWeight(stones))
    except Exception as e:
        print(e)
    finally:
        pass
