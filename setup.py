from setuptools import setup, find_packages

setup(
    name="ncert_learn",                   # Replace with your package name
    version="2.5.5",                     # Initial version
    author="Muhammed Shafin P",
    author_email="hejhdiss@example.com",
    description="A module for learning in ncerts cs class 12 python and mysql",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'mysql-connector-python',  # Add this line to include the MySQL connector
    ],
)
