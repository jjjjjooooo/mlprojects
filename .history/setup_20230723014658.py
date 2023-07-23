from distutils.core import setup
from setuptools import find_packages, setup





setup(name='mlprojects',
      version='1.0',
      description='Python Distribution Utilities',
      author='Ou Jin',
      author_email='jinoujoe@gmail.com',
      packages=find_packages()
      install_requires=['pandas', 'numpy', 'seaborn', 'matplotlib']
     )