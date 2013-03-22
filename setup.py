from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='whatapi',
    version='0.1.2',
    description='What.cd API',
    long_description=readme,
    author='Isaac Zafuta',
    author_email='isaac@zafuta.com',
    url='https://github.com/isaaczafuta/whatapi',
    license=license,
    install_requires = [
        "requests"
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    package_data = {
        '': ['*.txt']
    },
    zip_safe=True
)
