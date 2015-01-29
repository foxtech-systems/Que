from StartNode import StartNode

class Module(object):
    """Module represents a whole structure of a module in topology"""
    EntityTypes = []
    
    StartNodes = []
    MiddleNodes = []
    EndNodes = []

    #def AddNode(self, node):
    #    if isinstance(node, StartNode):
    #        if StartNodes.find(node) != -1:
    #            StartNodes.append(node)
    #    elif isinstance(node, MiddleNode):
    #        if MiddleNodes.find(node) != -1:
    #            MiddleNodes.append(node)
    #    elif isinstance(node, EndNode):
    #        if EndNodes.find(node) != -1:
    #            EndNodes.append(node)
    #    return self
    
    #def RemoveNode(self, node):
    #    if isinstance(node, StartNode):
    #        if StartNodes.find(node) != -1:
    #            StartNodes.remove(node)
    #    elif isinstance(node, MiddleNode):
    #        if MiddleNodes.find(node) != -1:
    #            MiddleNodes.remove(node)
    #    elif isinstance(node, EndNode):
    #        if EndNodes.find(node) != -1:
    #            EndNodes.remove(node)
    #    return self


