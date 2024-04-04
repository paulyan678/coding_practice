# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if node == None:
                # not rob, rob 
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)

            rob_val = left[0] + right[0] + node.val

            not_rob_val = max(left) + max(right)

            return not_rob_val, rob_val
        return max(dfs(root))


        