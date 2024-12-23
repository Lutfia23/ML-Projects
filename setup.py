from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

# Function to read the requirements from the requirements.txt file
def get_requirements(file_path:str)-> List[str]:
#This function will return the requirements....
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements
   

setup(
    name="ml-project",
    version="0.0.1",
    author="Nijhum",
    author_email="lutfianijhum.ruet.ece17@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
