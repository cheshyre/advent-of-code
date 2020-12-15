"""Module to create target dicts.
"""
from typing import Sequence, Dict, Tuple


def create_target_dict_pairs(components: Sequence[int], target: int) -> Dict[int, int]:
    """Create dict of remaining value to hit target.

    Args:
        components (Sequence[int]): Component integers that need to be added to target.
        target (int): Target integer value.

    Returns:
        Dict[int, int]: Dictionary with remaining value needed as key and other integer as value.

    """
    output_dict = {}
    for val in components:
        output_dict[target - val] = val
    return output_dict
    
    
def create_target_dict_triples(components: Sequence[int], target: int) -> Dict[int, Tuple[int, int]]:
    """Create dict of remaining values to hit target.

    Args:
        components (Sequence[int]): Component integers that need to be added to target.
        target (int): Target integer value.

    Returns:
        Dict[int, Tuple[int, int]]: Dictionary with remainig value needed as key and other two integers in tuple as value.
        
    """
    output_dict = {}
    for val1 in components:
        for val2 in components:
            if val1 != val2:
                output_dict[target - val1 - val2] = (val1, val2)
    return output_dict
