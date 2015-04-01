# encoding: utf-8

from distutils.core import setup
import sys

import linguo

version = linguo.__version__

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version(version, __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

setup(
    name='django-linguo',
    packages=['linguo', 'linguo.tests'],
    package_data={'linguo': ['tests/locale/*/LC_MESSAGES/*']},
    version=version,
    description=linguo.__doc__,
    long_description=open('README.md').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    author='Zach Mathew, UACF',
    url='http://github.com/underarmour/django-linguo',
    license='BSD',
)
