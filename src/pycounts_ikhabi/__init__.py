# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_ikhabi")

from pycounts_ikhabi.pycounts_ikhabi import count_words
from pycounts_ikhabi.plotting import plot_words