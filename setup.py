from setuptools import setup, find_packages

setup(
	name="base_project", 
	packages=find_packages(where="src"),
	package_dir={"": "src"},
	entry_points={
        'console_scripts': [
            'base_project=main:hello',
        ],
    },
)