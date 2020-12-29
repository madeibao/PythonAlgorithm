

# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        return self.check(sequence,0,len(sequence)-1)


    def check(self,arr,start,end):
        if start>=end:
            return True

        # 代表的是根节点的值。

        # 找到根节点的位置的值。
        root = arr[end]
        end = end - 1
        while(end >=0 and arr[end]>root):
            end -= 1
        mid = end + 1
        for i in range(start,mid):
            if arr[i] > root:
                return False
        return self.check(arr,start,mid-1) and self.check(arr,mid,end)


#============================================================================
#---------------------------------------------------------------------------------------------------

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder is None or len(postorder) == 0:
            return True
        n = len(postorder)
        # 根结点
        root = postorder[-1]
        # 在二叉搜索树中左子树的结点小于根结点
        i = 0
        for i in range(n):
            if postorder[i] > root:
                break

        # 如果右子树的节点小于根节点，那么一定是错误的。

        # 在二叉搜索树中右子树的结点小于根结点
        for j in range(i,n-1):
            if postorder[j] < root:
                return False

                
        # 判断左子树是不是二叉搜索树
        left = True
        if i > 0:
            left = self.verifyPostorder(postorder[:i])  # 左闭右开
        # 判断右子树是不是二叉搜索树
        right = True
        if i < n-1:
            right = self.verifyPostorder(postorder[i:-1])
        return left and right


if __name__ == "__main__":
    s =Solution()
    list2 = [1,3,2,6,5]
    print(s.VerifySquenceOfBST(list2))

    