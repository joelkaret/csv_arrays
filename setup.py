from setuptools import setup

packages = [
    'csv_arrays'
]

setup(name="csv_arrays.py",
    author="Joel Karet",
    author_email="joelkaret@gmail.com",
    url="https://github.com/joelkaret/csv_arrays.py",
    version="0.0.1",
    packages=packages,
    license='MIT',
    description="Helpful maniuplation in regards to arrays stored in CSV files.",
    #long_description = 
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
