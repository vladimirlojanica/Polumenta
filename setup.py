from setuptools import setup, find_packages

setup(
	name='polumenta',
	version='0.1',
	packages=find_packages(exclude=['tests*']),
	license='MIT',
	description='Polumenta generator',
	long_description=open('readme.md').read(),
	install_requires=[],
	url='',
	author='Vladimir Lojanica',
	author_email='vladimirlojanica@gmail.com'
)