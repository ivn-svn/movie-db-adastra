from setuptools import setup, find_packages

setup(
    name="MoviesAnalyzer",
    version="0.1.0",
    description="A simple movies dataset analyzer. Assignment for a job application.",
    author="Svetlin Ivanov",
    author_email="iv.svetlin@outlook.com",
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[
        "pandas>=1.2.0",
        "scipy>=1.5.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: AdAstra Reviewers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
