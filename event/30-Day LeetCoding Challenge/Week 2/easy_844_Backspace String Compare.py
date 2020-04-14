class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in range(max(len(S), len(T))):
            if i < len(S):
                if S[i] != '#':
                    s.append(S[i])
                else:
                    if s:
                        s.pop()
            if i < len(T):
                if T[i] != '#':
                    t.append(T[i])
                else:
                    if t:
                        t.pop()
        s = ''.join(s)
        t = ''.join(t)

        return s == t


if __name__ == "__main__":
    try:
        Solution = Solution()
        S = "y#fo##f"
        T = "y#f#o##f"
        print(Solution.backspaceCompare(S, T))
    except Exception as e:
        print(e)
    finally:
        pass
