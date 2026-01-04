"""
Setup script for Migration Engine
"""

from setuptools import setup, find_packages
import os

# Read README for long description
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="migration-engine",
    version="0.1.0",
    author="Migration Engine Team",
    description="ETL pipeline for migrating CSV data to PostgreSQL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5.0",
        "psycopg2-binary>=2.9.0",
        "python-dotenv>=0.19.0",
        "click>=8.0.0",
        "pyyaml>=6.0",
        "sqlalchemy>=1.4.0",
    ],
    entry_points={
        "console_scripts": [
            "migrate=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)