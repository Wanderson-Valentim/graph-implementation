class ExceptionVertexDoesNotExist(Exception):
    pass 

class ExceptionEdgeDoesNotExist(Exception):
    pass 

class ExceptionCouldNotAddEdge(Exception):
    pass 

class ExceptionInvalidOperation(Exception):
    pass 

class ExceptionUnableToRemoveEdge(Exception):
    pass

class ExceptionDoesNotHaveAPathFromViToVj(Exception):
    pass

class ExceptionContainsNegativeCycle(Exception):
    pass

class ExceptionGraphHasNoComplement(Exception):
    pass

class ExceptionThereIsNoFileWithThatName(Exception):
    pass