# This script generates a 6 alphanumerical character UUID. It is used for our DMSO stocks, Dosing Heads, and Compound Bottle Inventory. 

import random, string

def generate_uuid(size=6, chars=(string.ascii_uppercase + string.digits)):
    """
    Generate convenient universally unique id (UUID)
    Parameters
    ----------
    size : int, optional, default=6
       Number of alphanumeric characters to generate.
    chars : list of chars, optional, default is all uppercase characters and digits
       Characters to use for generating UUIDs
    NOTE
    ----
    This is not really universally unique, but it is convenient.
    """
    return ''.join(random.choice(chars) for _ in range(size))

print(generate_uuid())
