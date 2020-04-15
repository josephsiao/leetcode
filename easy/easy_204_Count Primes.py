class Solution:
    def countPrimes(self, n: int) -> int:
        is_primes = [True] * (n + 1)
        for i in range(2, int(n ** 0.5) + 1):
            if is_primes[i]:
                for j in range(i ** 2, n + 1, i):
                    is_primes[j] = False
        res = 0
        for i in range(2, n):
            if is_primes[i]:
                res += 1

        return res


if __name__ == "__main__":
    try:
        Solution = Solution()
        n = 10
        print(Solution.countPrimes(n))
    except Exception as e:
        print(e)
    finally:
        pass
