class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num_l1 = 0
        num_l2 = 0
        i = 0
        while l1 or l2:
            if l1:
                num_l1 += l1.val * (10 ** i)
                l1 = l1.next
            if l2:
                num_l2 += l2.val * (10 ** i)
                l2 = l2.next
            i += 1

        sum_num = num_l1 + num_l2

        new = dummy = ListNode(0)

        for i in range(len(str(sum_num))):
            new.next = ListNode(sum_num % 10)
            sum_num //= 10
            new = new.next

        return dummy.next


def create_ListNode(nums):
    root = temp = ListNode(nums[0])
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i])
        temp = temp.next

    return root


if __name__ == "__main__":
    try:
        Solution = Solution()
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        l1 = create_ListNode(l1)
        l2 = create_ListNode(l2)
        print(Solution.addTwoNumbers(l1, l2))
    except Exception as e:
        print(e)
    finally:
        pass
