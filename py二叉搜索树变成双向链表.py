
from typing import List

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None 

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        def link(list1, list2): # 将两个链表拼接后返回新的链表
            if not list1:
                return list2
            if not list2:
                return list1
            list2.left.right, list1.left.right  = list1, list2
            list1.left, list2.left = list2.left, list1.left
            return list1

        left_list = self.treeToDoublyList(root.left)
        right_list = self.treeToDoublyList(root.right)
        root.left, root.right = root, root # 将当前节点转换为只有一个节点的链表
        return link(link(left_list, root), right_list)


if  __name__ == "__main__":
    s = Solution()
    root = TreeNode(4)

    n2 = TreeNode(2)
    n3 = TreeNode(5)

    root.left = n2 
    root.right = n3

    n4 = TreeNode(1)
    n5 = TreeNode(3)

    n2.left =n4 
    n2.right =n5 #

    res = s.treeToDoublyList(root)

    count=0
    while res:
        print(res.val,end= "->")
        count+=1
        if count==5:break
        res= res.right

    
'''
C++的写法。


/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
private: 
    Node* head, *tail;
public:
    Node* treeToDoublyList(Node* root) {
        if(!root) {
            return nullptr;
        }

        inorder(root); // 构造出链表的所有结构，除了头连尾和尾连头的两个指针
        head -> left = tail; // 补上头连尾
        tail -> right = head; // 补上尾连头

        return head; // 返回头
    }
    void inorder(Node* root) {
        if(!root) {
            return;
        }

        inorder(root -> left); // 左

        if(!tail) {
            head = root;
        }
        else {
            tail -> right = root; // 前一个节点的right是当前节点
            root -> left = tail; // 当前节点的left是前一个节点
        }
        tail = root; // 将前一个节点更新为当前节点（所以到最后，tail就会挪到整个BST的最右边的节点，这个节点就是链表的尾节点）

        inorder(root -> right); // 右
    }
};

'''

