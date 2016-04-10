from setuptools import setup, find_packages

setup(
    name="diaphora",
    version="0.1",
    author="Joxean Koret",
    author_email="admin@joxeankoret.com",
    description=("A Free and Open Source program diffing tool"),
    license="GPLv2",
    keywords="diaphora ida diff bindiff disassembler",
    url="https://github.com/joxeankoret/diaphora",
    packages=find_packages(),
    install_requires=[
        'pygments'
    ]
)
