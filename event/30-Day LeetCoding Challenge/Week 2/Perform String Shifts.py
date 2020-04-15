from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        directions = {0: 0, 1: 0}
        for direction, amount in shift:
            directions[direction] += amount
        final_amount = abs(directions[0] - directions[1]) % len(s)
        final_direction = 0 if directions[0] > directions[1] else 1

        if final_direction == 0:
            return s[final_amount:] + s[0:final_amount]
        else:
            return s[len(s) - final_amount:] + s[:len(s) - final_amount]


if __name__ == "__main__":
    try:
        Solution = Solution()
        s = "xqgwkiqpif"
        shift = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6],
                 [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]
        print(Solution.stringShift(s, shift))
    except Exception as e:
        print(e)
    finally:
        pass
