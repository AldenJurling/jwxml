from setuptools import setup
from setuptools import find_packages

setup(
    name='jwxml',
    version='0.1.0',
    packages=find_packages(),
    package_data={'jwxml': ['test/test_surs/*.xml']},
    include_package_data=True,
    url='',
    license='',
    author='',
    author_email='',
    description='',
)
