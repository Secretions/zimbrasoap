#!/usr/bin/env python

from distutils.core import setup
try:
    import py2exe
    from nsis import build_installer
except:
    build_installer = None

import zimbrasoap

setup(name='zimbraSOAP',
      version=zimbrasoap.__version__,
      description='Python Zimbra SOAP API Library',
      author='Joaquin Lopez',
      author_email='mrgus@disco-zombie.net',
      packages=['zimbrasoap',],
      cmdclass = {"py2exe": build_installer},
     )

