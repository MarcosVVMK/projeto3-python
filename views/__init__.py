import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))

sys.path.append(current_directory)

from . import home
from . import add_product
from . import edit_product
from . import show_products