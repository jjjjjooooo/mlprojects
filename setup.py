from setuptools import find_packages, setup


hypen_e_dot = '-e .'
def get_requirements(file_path):
      '''Get the requirements'''
      requirements = []
      with open(file_path, 'r') as f:
            requirements=f.readlines()
            requirements=[req.replace('\n','') for req in requirements]

      if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
            
      return requirements


setup(
      name='mlprojects',
      version='1.0',
      description='Python Distribution Utilities',
      author='Ou Jin',
      author_email='jinoujoe@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt')
     )