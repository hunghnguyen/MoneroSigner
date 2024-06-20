import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MoneroSigner",
    version="0.3.3",
    author="MoneroSigner",
    author_email="author@example.com",
    description="Build an offline, airgapped Bitcoin signing device for less than $50!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DiosDelRayo/MoneroSigner",
    project_urls={
        "Bug Tracker": "https://github.com/DiosDelRayo/MoneroSigner/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
