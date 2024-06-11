from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = "-e ."
def get_requirements(file_paths: str) -> List[str]:
    requirements = []
    with open(file_paths) as file_obj:  # Corrected from "file_paths" to file_paths
        requirements = file_obj.readlines()  # Changed from readline to readlines to read all lines
        requirements = [req.strip() for req in requirements]  # Using strip() to remove whitespace and newlines

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements
        
    
setup(
    name = "ML_project",
    version = "0.0.1",
    author = "Keyur",
    packages = find_packages(),
    requirements = get_requirements(r"C:\Users\Keyur Mistry\Desktop\ML_project\requirements.txt")
)
 