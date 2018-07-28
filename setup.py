import setuptools

setuptools.setup(
    name="np_api",
    version="0.0.1",
    author="Bluefire",
    author_email="author@example.com",
    description="A python wrapper for the unofficial nhentai api",
    url="https://github.com/pypa/sampleproject",
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
