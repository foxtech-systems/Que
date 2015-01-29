class ProcessBase(object):
    """ProcessBase is the base of all kinds of Processes"""

    # Name represents a name of a Process
    Name = ""

    # Module represents the host Module of a Process
    Module = None

    def __init__(self, module):
        Module = module