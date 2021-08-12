from typing import List
import helper_functions.db_operations as db_op
from app import MONGO


def build_list_with_storage_sizes():
    """
    Builds a list with no repeating values of the unit sizes available
    """
    all_units = db_op.get_all_units()
    av_unit_sizes = []
    for unit in all_units:
        if unit['unit_size'] not in av_unit_sizes:
            av_unit_sizes.append(unit['unit_size'])
    
    return av_unit_sizes
