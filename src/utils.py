import os
import random
import string
from typing import Any, Dict, List, Optional

def flatten_dict(d: Dict[Any, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """
    Flattens a nested dictionary.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunks(lst: List[Any], n: int) -> List[List[Any]]:
    """
    Yield successive n-sized chunks from a list.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def set_seed(seed: int) -> None:
    """
    Set random seed for reproducibility in random and os.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
 
def random_string(length: int = 8) -> str:
    """
    Generates a random alphanumeric string.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def ensure_dir(path: str) -> None:
    """
    Creates a directory if it does not exist.
    """
    if not os.path.exists(path):
        os.makedirs(path)
 