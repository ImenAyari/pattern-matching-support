import setuptools
from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pattern-matching-support",
    version="0.0.1",
    author="Imen Ayari",
    author_email="ayari.imen@hotmail.com",
    description="POC for pattern matching",
    long_description=long_description,
    url="https://github.com/ImenAyari/pattern-matching-support.git",
    packages=["pattern_matching_support"],
    install_requires=[],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',
    ],
)
