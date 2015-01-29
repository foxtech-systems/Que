from ProcessBase import ProcessBase
class StartProcess(ProcessBase):
    """StartProcess represents a process that is a start point of a module"""

    def __init__(self, module):
        super(StartProcess, self).__init__(module)
