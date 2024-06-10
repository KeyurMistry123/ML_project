from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_paths: str)->List[str]:
    requirements = []
    with open("file_paths") as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n","") for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
            
    return requirements
        
    
setup(
    name = "ML_project",
    version = "0.0.1",
    author = "Keyur",
    packages = find_packages(),
    requirements = get_requirements("requirements.txt")
)
 