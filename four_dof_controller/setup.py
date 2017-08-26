#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['four_dof_controller'],
    package_dir={'': 'src'},
    )

setup(**d)

