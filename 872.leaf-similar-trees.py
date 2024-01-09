#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode],
    ) -> bool:
        def pre_order(node: TreeNode, sequence: List[int]):
            if not node:
                return

            if not node.left and not node.right:
                sequence.append(node.val)

            pre_order(node.left, sequence)
            pre_order(node.right, sequence)

        s1 = []
        s2 = []
        pre_order(root1, s1)
        pre_order(root2, s2)

        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True


# @lc code=end
