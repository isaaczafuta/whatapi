from setuptools import setup, find_packages
import whatapi

with open('README.txt') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='whatapi',
    version='0.0.1',
    description='What.cd API',
    long_description=readme,
    author='Isaac Zafuta',
    author_email='isaac@zafuta.com',
    url='https://github.com/isaaczafuta/whatapi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
