import math

# tree = [1,2,2,3,3,None,3,4,4,4,4,4,None,None,4]
#
# height = int(math.log2(len(tree)+1))
#
# newtree = []
#
# depth = 1
#
# for i in range(height):
#     templist = tree[depth-1:depth*2-1]
#     templist.reverse()
#     for i in templist:
#         newtree.append(i)
#     depth *=2
#
# print(newtree)
class invertTree:
    def __init__(self, treelist):
        self.tree = treelist
        self.height = int(math.log2(len(self.tree)+1))
        self.newtree = []
        self.depth = 1

        for i in range(self.height):
            templist = self.tree[self.depth-1:self.depth*2-1]
            templist.reverse()
            for i in templist:
                self.newtree.append(i)
            self.depth *=2
        return

        def __str__(self):
            return self.newtree


obj = invertTree([1,2,2,3,3,None,3,4,4,4,4,4,None,None,4])
print(obj.newtree)
