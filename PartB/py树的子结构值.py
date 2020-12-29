'''

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isSubStructure(TreeNode A, TreeNode B) {
        
        // 如果A或B都走完了还没找到，那应该就是找不到了
        if(A == null || B == null) return false;

        //看看当前节点成不？不成就看看左边，不然看看右边？
        return s(A,B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);
    }
    
    boolean s(TreeNode a, TreeNode b) {
        // b这边都看完了，还没挑出不同？那就是了吧！
        if(b == null) return true;
        // b这边还没看完了，a那边就null了？
        else if(a == null) return false;
        
        return a.val == b.val && s(a.left, b.left) && s(a.right, b.right);
    }
}
'''
#=======================================================================================================================================
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A==None or B==None:
            return False
        return self.sub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def sub(self, a, b):
        if b==None:
            return True
        elif a==None:
            return False
        return a.val ==b.val and self.sub(a.left, b.left) and self.sub(a.right, b.right)


if __name__ == "__main__":
    s =Solution()

    n2 = TreeNode(3)
    n3 = TreeNode(4)
    n4 = TreeNode(5)

    n2.left = n3
    n2.right = n4

    nM = TreeNode(1)
    nn = TreeNode(2)

    n3.left = nM
    n3.right = nn #


    m2 = TreeNode(4)
    m3 = TreeNode(1)
    m2.left = m3

    print(s.isSubStructure(n2, m2))

