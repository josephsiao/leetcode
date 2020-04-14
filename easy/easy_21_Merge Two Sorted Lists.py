class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        current = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if not l1:
            current.next = l2

        if not l2:
            current.next = l1

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
        l1 = [1, 2, 4]
        l2 = [1, 3, 4]
        l1 = create_ListNode(l1)
        l2 = create_ListNode(l2)
        print(Solution.mergeTwoLists(l1, l2))
    except Exception as e:
        print(e)
    finally:
        pass
