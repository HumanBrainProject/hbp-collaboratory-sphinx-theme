# -*- coding: utf-8 -*-
"""`hbp_collaboratory_sphinx_theme`
"""
from setuptools import setup
from hbp_collaboratory_sphinx_theme import __version__

import os

directory = os.path.abspath(os.path.dirname(__file__))

setup(
    name='hbp_collaboratory_sphinx_theme',
    version=__version__,
    license='HBP/EPFL all right reserved',
    url='https://github.com/HumanBrainProject/hbp-collaboratory-sphinx-theme',
    author='Olivier Amblet',
    author_email='olivier.amblet@epfl.ch',
    description='HBP Collaboratory theme for Sphinx',
    long_description=open(os.path.join(directory, 'README.rst')).read(),
    zip_safe=False,
    packages=['hbp_collaboratory_sphinx_theme'],
    package_data={'hbp_collaboratory_sphinx_theme': [
        'theme.conf',
        '**/*.html',
        'static/**/*.*',
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
)
