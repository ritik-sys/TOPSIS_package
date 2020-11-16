import setuptools

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="TOPSIS_Ritikkumar_101983054",  # Replace with your own username
    version="1.2.0",
    author="Ritik Kumar",
    author_email="rkumar2_be18@thapar.edu",
    description="Technique for Oder Preference by Similarity to Ideal Solution.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ritik-sys/TOPSIS_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
