from setuptools import setup, find_packages

setup(
    name='data_processing',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Data processing package (data pipeline)',
    long_description=open('README.md').read(),
    url="",
    author="Ebrahem Hassan",
    author_email="ebrahemhassan132001@gmail.com"
)