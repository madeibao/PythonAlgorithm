from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # 将 nums 转为集合，使查找时间复杂度降为 O(1)
        delete_set = set(nums)
        
        # 虚拟头节点，简化删除头节点的操作
        dummy = ListNode(-1)
        dummy.next = head
        
        # prev 始终指向“当前待检查节点”的前一个节点
        prev = dummy
        
        while prev.next:
            if prev.next.val in delete_set:
                # 发现需要删除的节点，跳过它
                prev.next = prev.next.next
            else:
                # 不需要删除，prev 指针后移
                prev = prev.next
                
        # 始终返回 dummy.next，而不是移动后的 prev
        return dummy.next

if __name__ == "__main__":
    nums = [1, 2, 3]
    # 构建链表 1->2->3->4->5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    
    s = Solution()
    node = s.modifiedList(nums, head)
    
    # 预期输出: 4 -> 5
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)