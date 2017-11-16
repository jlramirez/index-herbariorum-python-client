from setuptools import setup

setup(
      name='indexherbariorum',
      version='1.0.0',
      author='Joel Ramirez',
      author_email='joel.ramirez001@gmail.com',
      description='Python client library for Index Herbariorum API Web Services',
      license='MIT License',
      url='https://github.com/jlramirez/index-herbariorum-python-client',
      packages=['indexherbariorum'],
      install_requires=['requests'],
      long_description=open("README.rst").read(),
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ]
      )
