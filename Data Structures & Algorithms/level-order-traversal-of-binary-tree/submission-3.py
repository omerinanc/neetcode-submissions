# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root) # queue = [1]
        result = []

        while queue:
            level = []
            size = len(queue) # size = 1
            
            while size > 0:
                if queue:
                    for c in range(len(queue)):
                        level.append(queue[c]) # level = [1]
                if level:
                    for x in range(len(level)):
                        if level[x] in queue:
                            queue.remove(level[x]) # queue = []
                for i in range(len(level)):
                    if level[i] and level[i].left:
                        queue.append(level[i].left)
                        size -= 1
                    if level[i] and level[i].right:
                        queue.append(level[i].right)
                        size -= 1
                    if not level[i].right and not level[i].right: 
                        size = 0
            level_val = []
            for j in level:
                level_val.append(j.val)
            result.append(level_val)
        return result
                
                
                
                
                
