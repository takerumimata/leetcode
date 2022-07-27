# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head

#         prev = None
#         while(head):
#             curr = head
#             head = head.next
#             curr.next = prev
#             prev = curr


#         return curr

        # head [1, 2, 3, 4, 5]
        tmp = []
        while(head):
            tmp.append(head.val)
            head = head.next
        # tmp -> [1, 2, 3, 4, 5]

        ans = ListNode()
        ret = ans
        print(type(ans))
        print(tmp)

        for i in range(len(tmp)):
            print(tmp[-i - 1])
            ans.val = tmp[-i - 1]
            if(i == len(tmp) - 1):
                break
            ans.next = ListNode()
            ans = ans.next

        # ans.val = None
        return ret
