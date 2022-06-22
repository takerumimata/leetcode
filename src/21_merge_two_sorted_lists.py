from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ret = ListNode(0)
        # if list1 is None and list2 is None:
        #     ret.val = None
        #     return ret

        # while(list1 is not None or list2 is not None):

        #     # どちらかのvalがnullになった時点で、残ってる方をお尻に追加して終わり
        #     if list1 is None:
        #         while(list2 is not None):
        #             ret.val = list2.val
        #             ret = ret.next
        #             list2 = list2.next
        #     if list2 is None:
        #         while(list1 is not None):
        #             ret.val = list1.val
        #             ret = ret.next
        #             list1 = list1.next

        #     val1 = list1.val
        #     val2 = list2.val

        #     if val1 <= val2:
        #         ret.val = val1
        #         ret = ret.next
        #         list1 = list1.next
        #     else:
        #         ret.val = val2
        #         ret = ret.next
        #         list2 = list2.next
        # return ret

        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
