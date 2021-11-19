import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_arrays",
    version="0.0.1",
    author="Joel Karet",
    author_email="joelkaret@gmail.com",
    description="Helpful maniuplation in regards to arrays stored in CSV files",
    url="https://github.com/joelkaret/csv_arrays",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "csv_arrays"},
    packages=setuptools.find_packages(where="csv_arrays"),
    python_requires=">=3.6",
)
