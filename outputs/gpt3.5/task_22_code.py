# @Authors
# * Student Names: Name1, Name2, Name3
# * Student IDs: ID1, ID2, ID3


def filter_integers(values):
    """
    This function takes a list of values and filters out only the integers from the list.
    
    Parameters:
    values (list): A list of values
    
    Returns:
    integers (list): A list containing only the integers from the input list
    """
    
    integers = [value for value in values if isinstance(value, int)]
    
    return integers