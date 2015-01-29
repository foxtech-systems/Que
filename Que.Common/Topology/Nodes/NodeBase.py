from TopologyBase import TopologyBase
class NodeBase(TopologyBase):
    """NodeBase is the base of all kinds of Nodes"""
    Process = None

    def __init__(self, process):
        Process = process

    def GetProcess(self):
        return Process

