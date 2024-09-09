# setup.py
from setuptools import setup, find_packages

setup(
    name="storm-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "storm=storm_cli.main:app",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Storm CLI - A command-line tool for managing Storm applications.",
    url="https://github.com/Adi3g/storm-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
