from setuptools import setup, find_packages
from typing import List


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

PROJECT_NAME = "TextSummarizer"  # same as the name of your repo
AUTHOR_USER_NAME = "Zewen-Yang"
# SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "zewenreal@gmail.com"

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name=PROJECT_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    # long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{PROJECT_NAME}/issues",
    },
    package_dir={"": "src"},
    # where = src because the custom package is in src
    # also avoid using the package as src.TextSummarizer
    packages=find_packages(where="src"),  
    install_requires=get_requirements('requirements.txt'),
)


'''
packages=find_packages(): searches for packages by looking for __init__.py files 
(which indicate a package) within directories specified by the where parameter 
(if provided) or the current directory (if where is not provided). 
'''

'''
The main purpose of the setup.py file is to define the project's setup configuration, 
which includes the metadata and instructions for building, packaging, and distributing the project. 
It allows users to easily install the project, either for development purposes or as a library or application dependency.

With the setup.py file in place, you can use tools like pip to install the project, 
distribute it to others, or publish it on package indexes such as PyPI (Python Package Index). 
It provides a standardized and convenient way to manage the packaging and distribution of Python projects.

you will find a folder named ending with .egg-info
'''

