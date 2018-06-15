# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        

    def printList(self, node):
        # s = "aaba"
        # print(s)
        tmpNode = node
        while tmpNode != None:
            print(tmpNode.val)
            tmpNode = tmpNode.next
     

if __name__ == '__main__':
    n1 = ListNode(4)
    n2 = ListNode(8)
    n3 = ListNode(7)
    n1.next = n2
    n2.next = n3

    t = Solution()
    t.printList(n1)
    # t.deleteNode("hello")
     