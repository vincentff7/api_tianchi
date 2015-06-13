#-*-coding=utf-8-*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

packages = []

setup(name='tianchi',
      version='1.0',
      description='shushanbj',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: tornado",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='shushanbj',
      author_email='shushan_uestc@163.com',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tianchi',
      install_requires=packages,
      entry_points="""\
      [paste.app_factory]
      main = tianchi:main
      [console_scripts]
      initialize_tianchi_db = tianchi.scripts.initializedb:main
      """,
      )


