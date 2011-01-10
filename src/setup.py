from distutils.core import setup
import sys
import py2exe

mfcfiles = [join(mfcdir, i) for i in ["mfc90.dll"  "mfc90u.dll"  "mfcm90.dll"  "mfcm90u.dll"  "Microsoft.VC90.MFC.manifest"]]

data_files = [("Microsoft.VC90.MFC", mfcfiles),
              ]

setup(
    data_files = data_files,
    ...
  )

sys.argv.append('py2exe')

setup( console=["loader.py"] )
