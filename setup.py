from setuptools import setup, find_packages

setup(
    name="christmas_orchestrator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "naptha-sdk",
        "browser-use-sdk"
    ],
)
