from setuptools import setup, find_packages

setup(
    name="MoviesAnalyzer",
    version="0.1.0",
    description="A simple movies dataset analyzer",
    author="Svetlin Ivanov",
    author_email="iv.svetlin@outlook.com",
    packages=find_packages(),  # Automatically find all packages in the directory
    install_requires=[
        "bokeh==3.2.2",
        "contourpy==1.1.0",
        "Jinja2==3.1.2",
        "MarkupSafe==2.1.3",
        "numpy==1.25.2",
        "packaging==23.1",
        "pandas==2.0.3",
        "Pillow==10.0.0",
        "python-dateutil==2.8.2",
        "pytz==2023.3",
        "PyYAML==6.0.1",
        "scipy==1.11.2",
        "six==1.16.0",
        "tornado==6.3.3",
        "tzdata==2023.3",
        "xyzservices==2023.7"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
