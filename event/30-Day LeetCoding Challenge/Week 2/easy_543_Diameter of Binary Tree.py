# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max = 0

        def find_depth(tree_node: TreeNode) -> int:
            if not tree_node:
                return 0
            left = find_depth(tree_node.left)
            right = find_depth(tree_node.right)
            self.max = max(self.max, left + right)

            return 1 + max(left, right)

        find_depth(root)

        return self.max


def create_TreeNode():
    tree_node = TreeNode(1)
    tree_node.right = TreeNode(3)
    tree_node.left = TreeNode(2)
    tree_node.left.left = TreeNode(4)
    tree_node.left.right = TreeNode(5)

    return tree_node


if __name__ == "__main__":
    try:
        Solution = Solution()
        root = create_TreeNode()
        print(Solution.diameterOfBinaryTree(root))
    except Exception as e:
        print(e)
    finally:
        pass
