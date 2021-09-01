from setuptools import (
  setup,
  find_namespace_packages
)

with open(file="README.md", mode="r") as readme_handle:
  long_description = readme_handle.read()

setup(
  name='Doctor',
  author='Elliott Phillips',
  author_email='ellsphillipsuni@gmail.com',
  version='0.0.2',
  description='An automated documentation assistant built in Python and TeX for procedural, data-driven reporting.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='https://github.com/ellsphillips/doctor',
  keywords='python, latex, report-generator ',
  packages=find_namespace_packages(
    where=['doctor', 'doctor.*']
  ),
  include_package_data=True,
  python_requires='>=3.8',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Technical report writers',
    'License :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
  ]
)
