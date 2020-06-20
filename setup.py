import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QISKit-Graph-States",  # Replace with your own username
    version="0.0.7",
    author="Amelie Schreiber",
    author_email="thesingularity.research@gmail.com",
    description="Graph states for MBQC, error correction, and quantum cryptography",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    install_requires=[
        "networkx",
        "qiskit",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
