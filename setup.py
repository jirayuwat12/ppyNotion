import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_requirements(fname : str):
    '''
    extract library name from `fname`
    '''
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")


setuptools.setup(
    name="ppyNotion",
    version="0.0.1.3",
    author="jirayuwat b.",
    author_email="jirayuwat.work@gmail.com",
    description="Connect to your Notion database with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jirayuwat12/ppyNotion",
    install_requires = install_requires,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)