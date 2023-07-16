import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ppyNotion",
    version="0.0.1",
    author="jirayuwat b.",
    author_email="jirayuwat.work@gmail.com",
    description="Connect to your Notion database with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jirayuwat12/ppyNotion",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)