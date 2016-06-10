import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import dtim


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='dtim',
    packages=['dtim'],
    version=dtim.__version__,
    description='datetime improvement for standard datetime.datetime',
    long_description=read('README.rst'),
    author='Cuong Manh Le',
    author_email='cuong.manhle.vn@gmail.com',
    license='BSD',
    url='https://github.com/Gnouc/dtim',
    keywords=['datetime']
)
