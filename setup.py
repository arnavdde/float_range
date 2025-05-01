from setuptools import setup, find_packages

setup(
    name='float_range',
    version='0.1',
    description='A floating-point range generator for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Anushka',
    packages=find_packages(),
    install_requires=['numpy'],
    python_requires='>=3.6',
)
