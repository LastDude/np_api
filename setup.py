import setuptools

setuptools.setup(
    name="np_api",
    version="0.0.2",
    author="LastDude",
    author_email="LetsPlayHansLP@gmail.com",
    description="A python wrapper for the unofficial nhentai api",
    url="https://github.com/LastDude/np_api",
    packages=["np_api"],
    license="MIT",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
          'grequests', "bs4", "lxml", "requests"
      ]
)
