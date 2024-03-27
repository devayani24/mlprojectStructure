# find_packages helps to find entire machine learning packages in PyPI
from setuptools import find_packages,setup
from typing import List


# "-e ." is included at the end of requirements.txt. Therefore, it automatically runs setup.py when pip install -r requirements.txt is run on the cmd. 
# This avoids the necessary to explicitily run the command setup.py.
# Also we have to remove "-e ." in the list while reading the file.

HYPEN_E_DOT= "-e ."

def get_requirements(file_path)->List[str]:

    '''
    This function will return the list of requirements
    '''
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[r.replace("\n",'') for r in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    

    return requirements



# metadata of the entire package
setup(
    name="mlproject",
    version="0.0.1",
    author="deva",
    author_email='devayanisenvel@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)