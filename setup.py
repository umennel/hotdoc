import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mddoc",
    version="0.0.1",
    author="Uche Mennel",
    author_email="umennel@gmx.ch",
    description="A small script to generate beautiful HTML Documents from Markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umennel/mddoc",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={
        'mddoc': ['default.html'],
    },
    install_requires=['markdown', 'jinja2'],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'mddoc=mddoc.__main__:main',
        ],
    },
)
