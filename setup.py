from setuptools import setup, find_packages

setup(
    name="fastapi-dlna",
    version="0.1.0",
    description="A test DLNA Media server using fastapi",
    url="https://github.com/dereisele/VideoServer",
    author="Alexander Eisele",
    author_email="alexander@eiselecloud.de",
    license="GPL",
    install_requires=[
        "fastapi",
        "xmltodict",
        "uvicorn"
    ],
    packages=find_packages()
)
