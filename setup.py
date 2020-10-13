#!/usr/bin/env python
# coding: utf-8

r"""ydeos_benchmark setup.py."""

from distutils.core import setup

import ydeos_benchmark


setup(name=ydeos_benchmark.__project_name__,
      version=ydeos_benchmark.__version__,
      description=ydeos_benchmark.__description__,
      long_description='Benchmarking utilities to guard '
                       'against performance regressions.',
      url=ydeos_benchmark.__url__,
      download_url=ydeos_benchmark.__download_url__,
      author=ydeos_benchmark.__author__,
      author_email=ydeos_benchmark.__author_email__,
      license=ydeos_benchmark.__license__,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3.7'],
      keywords='benchmark',
      packages=['ydeos_benchmark'])
