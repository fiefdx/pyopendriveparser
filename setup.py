#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='opendriveparser',
      version='1.0',
      description='Parser for files in OpenDRIVE format, offers additional functions to navigate through the road network',
      author='Stefan Urban',
      author_email='stefan.urban@live.de',
      url='https://github.com/stefan-urban/pyopendriveparser',
      packages=find_packages(),
      dependency_links=[
          'https://github.com/stefan-urban/pyeulerspiral/archive/master.zip#egg=pyeulerspiral-1.0',
      ],
      install_requires=[
          "numpy",
          "lxml",
          'pyeulerspiral==1.0',
      ]
     )
