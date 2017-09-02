#!/usr/bin/env python

from distutils.core import setup

setup(name='opendriveparser',
      version='1.0',
      description='Parser for files in OpenDRIVE format, offers additional functions to navigate through the road network',
      author='Stefan Urban',
      author_email='stefan.urban@live.de',
      url='https://github.com/stefan-urban/pyopendriveparser',
      packages=['opendrive-parser'],
      install_requires=[
            "numpy",
            "lxml",
            "https://github.com/stefan-urban/pyeulerspiral/archive/master.zip",
      ],
     )
