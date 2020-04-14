class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_square(n):
            nums = [int(i) for i in str(n)]
            result = 0
            for element in nums:
                result += element ** 2
            return result

        turtle_num = sum_of_square(n)
        rabbit_num = sum_of_square(sum_of_square(n))

        while turtle_num != 1 and turtle_num != rabbit_num:
            turtle_num = sum_of_square(turtle_num)
            rabbit_num = sum_of_square(sum_of_square(rabbit_num))

        return turtle_num == 1


if __name__ == "__main__":
    try:
        Solution = Solution()
        n = 2
        print(Solution.isHappy(n))
    except Exception as e:
        print(e)
    finally:
        pass
