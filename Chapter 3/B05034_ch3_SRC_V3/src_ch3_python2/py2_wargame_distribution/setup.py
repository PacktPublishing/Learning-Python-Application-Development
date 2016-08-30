from distutils.core import setup

with open('README') as file:
    readme = file.read()

# NOTE: change the 'name' field below with some unique package name.
# then update the url field accordingly.

setup(
    name='testgamepkg_uniquename',
    version='2.0.0',
    packages=['wargame'],
    url='https://testpypi.python.org/pypi/testgamepkg_uniquename/',
    license='LICENSE.txt',
    description='test pkg ignore',
    long_description=readme,
    author='your_name',
    author_email='your_email'
)

