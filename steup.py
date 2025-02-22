from setuptools import setup, find_packages

setup(
    name="my_nlp",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    description="A simple NLP preprocessing package",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zagane Mohammed Mounir",
    author_email="mounir.zagane@example.com",
    url="https://github.com/StrangeVlad/NLP_Package_Python",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
