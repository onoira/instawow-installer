import sys
from distutils.core import setup

import py2exe

sys.argv = [sys.argv[0], 'py2exe'] + sys.argv[1:]
setup(
    options={'py2exe': {'unbuffered': True}},
    console=['dl.py'],
    data_files=[('.', ['dl.cfg'])],
    zipfile="lib/shared.zip"
)
