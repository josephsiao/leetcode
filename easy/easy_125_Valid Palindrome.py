class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphas = []
        for element in s:
            if element.isalpha() or element.isdigit():
                alphas.append(element)

        for i in range(len(alphas)):
            if alphas[i] != alphas[len(alphas) - 1 - i]:
                return False

        return True


if __name__ == "__main__":
    try:
        Solution = Solution()
        s = "A man, a plan, a canal: Panama"
        print(Solution.isPalindrome(s))
    except Exception as e:
        print(e)
    finally:
        pass
