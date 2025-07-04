from setuptools import setup, find_packages

setup(
    name="sentiment",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
    ],
    author="Sandeep Singhal",
    author_email="sandeepsinghal@gmail.com",
    description="A package for sentiment analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sandeepsinghal/sentiment",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)