class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next

        for _ in range(count // 2):
            head = head.next

        return(head)


def create_ListNode(nums):
    root = temp = ListNode(nums[0])
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i])
        temp = temp.next

    return root


if __name__ == "__main__":
    try:
        Solution = Solution()
        nums = [1, 2, 3, 4, 5, 6]
        nums = create_ListNode(nums)
        print(Solution.middleNode(nums))
    except Exception as e:
        print(e)
    finally:
        pass
