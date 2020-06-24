from setuptools import find_packages, setup


setup(
    name="infraestructure",
    version="0.1.0",
    description="Infraenstructure manager module",
    packages=find_packages(),
    install_requires=["injector","accounts"]
)