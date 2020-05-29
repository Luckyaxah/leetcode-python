    # def getKthNode(self, k, node):
    #     cur = node
    #     while cur:
    #         cur_size = node.size
    #         right_size = node.right.size
    #         left_size = node.left.size
    #         if k <= cur_size-right_size:
    #             if left_size<k:
    #                 return cur
    #             cur = node.left
    #         else:
    #             cur = node.right