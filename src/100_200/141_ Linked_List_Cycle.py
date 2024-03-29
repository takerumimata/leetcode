# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """hashに探索したnodeを保存しておき、既知がどうか検査
        """
        hash_table = {}

        cur = head
        while(cur):
            # hash tableに値に格納。既にある場合はreturn true
            if(hash_table.get(cur)):
                return True
            hash_table[cur] = 1
            cur = cur.next
        return False
