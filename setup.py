#responsible in creating my machine learning application as a package 
#and deploy in pypi and anybody can install the application from there
from pip._internal.cli.main import main
from setuptools import find_packages,setup
from typing import List,Optional
# to find where to install the packages,find_packages will see in which folder __init__.py file is present and 
#that folder will be considered as package and can be import anywhere
#setup(
#name='mlproject_insurance',
#version='0.0.1',
#author='Anamika'
#author_email='mittal.anamika17@gmail.com',
#packages=find_packages(),
#install_requires=['pandas','numpy','seaborn','matplotlib']  
# # if I have to install multiple packages, not possible to mention here
# so we create a function get_requirements
#)



HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will require list of requiremnts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements




setup(
name='mlproject_insurance',
version='0.0.1',
author='Anamika',
author_email='mittal.anamika17@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)