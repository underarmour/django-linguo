from distutils.core import setup

import linguo


setup(
    name='django-linguo',
    packages=['linguo', 'linguo.tests'],
    package_data={'linguo': ['tests/locale/*/LC_MESSAGES/*']},
    version=linguo.__version__,
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
