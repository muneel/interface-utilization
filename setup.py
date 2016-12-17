#coding:utf-8

from setuptools import setup, find_packages

setup(	name="interface-utilization",
		version="0.1",
		packages=find_packages(),
		install_requires=[],
		py_modules = ['intutil'],
		entry_points = {
       			 'console_scripts': ['intutil=intutil:run_main'],
   			 },
		author="Muneel",
		author_email="muneel@hotmail.com",
		description="Tool to get Network Interface Utilization"
		)
