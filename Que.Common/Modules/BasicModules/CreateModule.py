import ModuleBase
import DistributionExpression
class CreateModule(ModuleBase):
    """
    CreateModule is used to create entities. 
    CreateModule is the start of a topology.
    """
    DistributionExpression = "EXPO(10)"
    EntitiesPerArrival = 1
    MaxArrivals = 0
    FirstCreation = 0.0


