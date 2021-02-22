import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Twitter_web_map",
    version="0.0.1",
    author="Pasichnyk Mykhailo",
    author_email="mykhailo.pasichnyk@ucu.edu.ua",
    description="Web-map based on Twitter API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fox-flex/Twitter_web_map.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

