"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        if not node:
            return 
        nodeDic = self.bfs(node)
        newNodeDic = {}
        for label in nodeDic:
            newNodeDic[label] = UndirectedGraphNode(label)
        for label in nodeDic:
            for nNode in nodeDic[label].neighbors:
                newNodeDic[label].neighbors.append(newNodeDic[nNode.label])
        for i in newNodeDic:
            return newNodeDic[i]
        
    def bfs(self, node):
        nodeDic = {}
        nodeList = []
        nodeList.append(node)
        while nodeList:
            tmpNode = nodeList.pop()
            if tmpNode.label not in nodeDic:
                nodeDic[tmpNode.label] = tmpNode
            for nNode in tmpNode.neighbors:
                if nNode.label not in nodeDic:
                    nodeList.insert(0, nNode)
        return nodeDic