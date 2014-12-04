#!/home/rhp/.virtualenvs/pytroll/bin/python


import sys

sys.path.append("/home/rhp/workspace/workflow/readers")
print(sys.path)

import importlib
m = 'txt_reader'
mod = importlib.import_module(m)
clazz = getattr(mod, "TXTFileReader")
oi = clazz()
print oi