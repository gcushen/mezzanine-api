import os
import sys
from setuptools import setup, find_packages
from mezzanine_api import __version__ as version

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if sys.argv[:2] == ["setup.py", "bdist_wheel"]:
    # Remove previous build dir when creating a wheel build
    try:
        rmtree("build")
    except:
        pass

setup(
    name='mezzanine-api',
    version=version,
    author='George Cushen',
    author_email='mezzanine-users@googlegroups.com',   
    url='http://github.com/gcushen/mezzanine-api',   
    description='A RESTful web API for Mezzanine CMS.',
    long_description=open("README.rst", 'rb').read().decode('utf-8'),
    keywords='mezzanine rest restful web api',
    include_package_data=True,
    license='BSD License',   
    packages=find_packages(),
    install_requires=[
        "mezzanine",
        "django-rest-swagger==0.2.9",
        "djangorestframework==3.1.1",
        "markdown",
        "django-filter"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
