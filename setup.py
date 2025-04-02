from setuptools import setup, find_packages

setup(
    name="SIxthStreet2025",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Tim Phan",
    author_email="phanmtim@gmail.com",
    description="A Python library for fetching stock quotes from Alpha Vantage",
    url="https://github.com/phanmtim/SIxthStreet2025",
)