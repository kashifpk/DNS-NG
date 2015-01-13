import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'twisted',
    'SQLAlchemy',
    'transaction',
    'psycopg2'
]

if sys.version_info[:3] < (2, 5, 0):
    requires.append('pysqlite')

# Requires from subapps
from compulife.apps import enabled_apps
for enabled_app in enabled_apps:
    if hasattr(enabled_app, 'app_requires'):
        for requirement in enabled_app.app_requires:
            if requirement not in requires:
                requires.append(requirement)

setup(
    name='compulife',
    version='0.6',
    description='compulife',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Twisted",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Topic :: Internet :: Name Service (DNS)"
    ],
    author='Kashif Iftikhar',
    author_email='kashif@compulife.com.pk',
    url='http://www.compulife.com.pk/dns_ng',
    keywords='DNS Spoofing MITM MIM Man-in-Middle-Attack',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    data_files=[('/etc/dnsng/', ['dnsng.ini'])],
    entry_points="""\
    [console_scripts]
    compulife_populate = compulife.scripts.populate:main
    compulife_newapp = compulife.scripts.newapp:main
    """,
)
