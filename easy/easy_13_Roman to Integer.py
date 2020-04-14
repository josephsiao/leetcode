class Solution:
    table = {
        'I':         1,
        'V':         5,
        'X':        10,
        'L':        50,
        'C':       100,
        'D':       500,
        'M':      1000
    }

    def romanToInt(self, s: str) -> int:
        total = 0
        for index, element in enumerate(s):
            if index > 0 and self.table[element] > self.table[s[index - 1]]:
                total += self.table[element] - 2 * self.table[s[index - 1]]
            else:
                total += self.table[element]

        return total


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = "DCCLXXXIV"   # 1 - 3999
        print(Solution.romanToInt(x))
    except Exception as e:
        print(e)
    finally:
        pass
