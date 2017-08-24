from setuptools import setup


setup(
    name='clientservergenerator',
    version='0.1',
    packages=['server_generator', 'configurator', 'client_generator'],
    install_requires=['pyyaml'],
)
