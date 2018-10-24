import platform
import re
import sys, os

from setuptools import Extension, setup
from setuptools.command.install import install
from subprocess import call

if sys.version_info < (3, 5):
	raise Exception('Only Python 3.5 and above are supported.')
	
with open('LICENSE', 'r') as legal:
	license = " ".join(line.strip() for line in legal)
	
class customInstallClass(install):
	def run(self):
		install.run(self)
		os.system("chmod +x ./install.sh")
		os.system("sh install.sh")
	

setup(
	name='nautilus-extension-jupyter',
	author='Aly Shmahell',
	author_email='aly.shmahell@gmail.com',
	license=license,
	url='https://github.com/AlyShmahell/nautilus-extension-jupyter',
	cmdclass={'install': customInstallClass}
)