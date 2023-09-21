# Importing all parts of the module
__all__ = ["currency_converter", "Diff_integr", "evaluate", "length_converter",
           "mass_converter", "volume_converter"]

from .Diff_integr import diffr, integr
from .evaluate import evaluation, fact, trig_fxn, modulo
from .currency_converter import converter
from .volume_converter import to_milimeter, milimeter_to, volconvert
from .length_converter import to_microns, microns_to, lenconvert
from .mass_converter import to_miligrams, miligrams_to, mass_convert
