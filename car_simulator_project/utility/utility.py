def get_root_package() -> str:
    """Gets the root name of current package.
    
    Returns:
        str: Directory name of current package.
    """
    return __package__.split(".")[0]