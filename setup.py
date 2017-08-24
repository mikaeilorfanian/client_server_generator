from setuptools import setup


setup(
    name='clientservergenerator',
    version='0.1',
    packages=['server_generator', 'configurator'],
    install_requires=['pyyaml', 'requests'],
)
