"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

	def maxDepth(self, root: TreeNode) -> int:
		if root == None:
			return 0
		left_height = self.maxDepth(root.left)
		right_height = self.maxDepth(root.right)
		return max(left_height, right_height) + 1