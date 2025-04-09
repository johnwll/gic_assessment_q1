class Result:
    """Returning result. By status, it can contain error or returning object.
    
    Attributes:
        status: (bool) Status of the result. True indicates no error, otherwise False.
        error: (str) Error message in string.
        object: (object) Result object to be returned if status is successful.
    """
    def __init__(self, status: bool, error: str = "", object = None):
        """Initialization.

        Arguments:
            status: (bool) Status of the result. True indicates no error, otherwise False.
            error: (str) Error message in string.
            object: (object) Result object to be returned if status is successful.
        """
        self.status = status
        self.error  = error
        self.object = object

    def ok(self) -> bool:
        """Check status is ok.
        
        Returns:
            bool - True if status is true, otherwise False.
        """
        return self.status