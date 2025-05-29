from setuptools import setup, find_packages

setup(
    name="types-keyboard",
    version="0.13.2.6",
    description="Type hints (stub) for the 'keyboard' module",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="kongali1720",
    author_email="kongali1720@gmail.com",
    url="https://github.com/kongali1720/types-keyboard",
    packages=find_packages(),
    package_data={"keyboard": ["__init__.pyi"]},
    classifiers=[
        "Typing :: Stubs Only",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    zip_safe=False,
)
