from StartProcess import StartProcess
class CreateProcess(StartProcess):
    """CreateProcess represents a start point which generates entities"""

    Type = None

    # DistributionExpression represents a distrubution of a Create in formular.
    #DistributionExpression = "CONSTANT(600)"
    Distribution = None
   
    #EntitiesPerArrival represents a number of entities that are generated each time.
    EntitiesPerArrival = 1

    # MaxArrivals
    MaxArrivals = 0

    # FirstCreation represents the time when the first entity is created
    FirstCreation = 0.0

    def __init__(self, module):
        super(StartProcess, self).__init__(module)
