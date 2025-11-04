from setuptools import setup, find_packages

setup(
    name="log_colors",
    version="0.1.0",
    packages=find_packages(),
    description="A colorful logging library for Python",
    long_description=open("README.md").read(),
    author="avery-kb",
    install_requires=[],
    python_requires=">=3.7",
    url="https://github.com/avery-kb/log_colors",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
