class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printList(self, node):
        # s = "aaba"
        # print(s)
        print("node:")
        tmpNode = node
        while tmpNode != None:
            print(tmpNode.val)
            tmpNode = tmpNode.next

    # 例如：
    # 输入：342
    # 输出：(2 -> 4 -> 3)

    def createList(self, num):
        """
        :type num: int number
        :rtype: ListNode
        """
        result = None
        last = None  # 最新的节点
        while num >= 0:
            n = ListNode(num % 10)
            if result == None:
                result = n

            if last != None:
                last.next = n
            last = n

            num = num // 10
            if num == 0:
                num = -1

        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        last = None
        carry = 0  # 进位
        while l1 != None or l2 != None or carry != 0:
            num = carry
            if l1 != None:
                num = num + l1.val
                l1 = l1.next
            if l2 != None:
                num = num + l2.val
                l2 = l2.next
            n = ListNode(num % 10)

            if result == None:
                result = n

            if last != None:
                last.next = n
            last = n

            carry = num // 10

        return result


if __name__ == '__main__':
    t = Solution()
    n1 = t.createList(5)
    t.printList(n1)
    n2 = t.createList(5)
    t.printList(n2)

    n3 = t.addTwoNumbers(n1, n2)
    t.printList(n3)
