import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("mceffects/__init__.py", encoding="utf-8") as f:
    exec(f.read())

setuptools.setup(
    name="mceffects",
    version=__version__,
    author="albi-c",
    description="minecraft particle effect generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/albi-c/mceffects",
    project_urls={
        "Bug Tracker": "https://github.com/albi-c/mceffects/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": {
            "mceffects = mceffects.cli:main"
        }
    }
)
