# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # print([1,2,4])
        """
        思路是从根节点开始，先将根节点压入栈，
        然后再将其所有左子结点压入栈，
        然后取出栈顶节点，保存节点值，
        再将当前指针移到其右子节点上，
        若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中。
        这样就保证了访问顺序为左-根-右，
        """
        res = [] # result
        s = [] # stack
        p = root
        while (p != None or len(s) > 0):
            while (p != None):
                s.append(p)
                p = p.left
            
            p = s.pop()
            res.append(p.val);
            p = p.right

        # print(res)
        return res

if __name__ == '__main__':
    t = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    t.inorderTraversal(n1)
     