from setuptools import setup, find_packages

setup(
    name="ncert_learn",                   # Replace with your package name
    version="4.2.1",                     # Initial version
    author="Muhammed Shafin P",
    author_email="hejhdiss@example.com",
    description="A Python Module for NCERT Class 12 Computer Science - Learn Python and MySQL with ease!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/hejhdiss/ncert_learn",  # Add your GitHub repository URL here
    project_urls={
        "Bug Tracker": "https://github.com/hejhdiss/ncert_learn/issues",
        "Documentation": "https://hejhdiss.github.io/ncert_learn-website/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'mysql-connector-python',
        'pytest',
        'tox',
        'requests',
        'psutil',
        'beautifulsoup4',
        'googlesearch-python',
        'python-nmap',
        
        # Add this line to include the MySQL connector
    ],
)
