import find_packages,setup
from typing import List

hyphen_e='-e .'
# The below function locate the requirement file and take the librariers as a list
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)

    return requirements


setup(
    name="ARUNKUMAR V",
    version='0.0.1',
    author_email='oyeahitsarunkumar@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)