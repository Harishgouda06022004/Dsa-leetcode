# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened_list = flatten_arr(nestedList)
        self.index = 0 
    
    def next(self) -> int:
        val=self.flattened_list[self.index]
        self.index+=1
        return val
    
    def hasNext(self) -> bool:
        return self.index<len(self.flattened_list)
def flatten_arr(nestedList):
    result = []
    for item in nestedList:
        if item.isInteger():  # If it's an integer, append directly
            result.append(item.getInteger())
        else:  # If it's a list, recursively flatten it
            result.extend(flatten_arr(item.getList()))
    return result
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
