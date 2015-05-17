from __future__ import print_function
import os
import sys
import re
from setuptools import setup, find_packages


def get_version(package):
    """Return package version as listed in `__version__` in `init.py`."""
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(get_version("mezzanine_api")))
    print("  git push --tags")
    sys.exit()


setup(
    name='mezzanine-api',
    version=get_version("mezzanine_api"),
    author='George Cushen',
    author_email='mezzanine-users@googlegroups.com',   
    url='http://gcushen.github.io/mezzanine-api',
    description='A RESTful web API for Mezzanine CMS.',
    long_description=open("README.rst", 'rb').read().decode('utf-8'),
    keywords='mezzanine rest restful web api',
    include_package_data=True,
    license='BSD',
    packages=find_packages(),
    install_requires=[
        "Mezzanine",
        "django-rest-swagger==0.2.9",
        "djangorestframework==3.1.1",
        "django-filter",
        "django-oauth-toolkit==0.8.1"
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
