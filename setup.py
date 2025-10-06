''' 
The setup.py file is an essential part of a packaging and distribution of a Python project.
It is used to specify metadata about the project, its dependencies, and how it should be installed.
This file is typically used with setuptools, a popular library for packaging Python projects.
It allows developers to easily share and distribute their code with others, making it easier to install and manage dependencies.
'''
## Find Packages is used to find all packages in the project directory

from setuptools import setup, find_packages

def get_requirements():

    """This function will return the list of requirements"""
    requirement_lst=[]
    try:
        with open("requirements.txt", "r") as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
         
            
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name="MLProject",
    version="0.0.1",
    author="Kapoor",
    author_email="kapoor.cheenu1999@gmail.com",
    packages=find_packages(), 
    install_requires=get_requirements()

)
