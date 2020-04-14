class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        elif len(s) % 2 != 0:
            return False
        else:
            pass
            parentheses = []
            parentheses_pair = {')': '(',
                                ']': '[',
                                '}': '{'}

            for element in s:
                if element in '([{':
                    parentheses.append(element)
                    pass
                elif element in ')]}':
                    try:
                        if parentheses[-1] == parentheses_pair[element]:
                            parentheses.pop()
                        else:
                            return False
                    except IndexError:
                        return False
                else:
                    return False

            if len(parentheses) != 0:
                return False

            return True


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = ')[]'
        print(Solution.isValid(x))
    except Exception as e:
        print(e)
    finally:
        pass
