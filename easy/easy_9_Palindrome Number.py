class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reverse = 0

        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        return True if x == reverse or x == reverse // 10 else False


if __name__ == "__main__":
    try:
        Solution = Solution()
        x = 1120211
        print(Solution.isPalindrome(x))
    except Exception as e:
        print(e)
    finally:
        pass
