from setuptools import setup, find_packages

setup(
    description="an Asynchronous Request Handler for sending a high volume of HTTP requests with variable headers and algorithmic scheduling to prevent IP blocking.",
    author="Mohammad Hossein Niksefat",
    author_email="mohammadhniksefat@gmail.com",
    url="github.com/mohammadhniksefat/requesthandler",
    name="requesthandler",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.11.18"
    ]
)
