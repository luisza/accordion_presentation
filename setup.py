from setuptools import setup, find_packages
setup(
    name='accordion_presentation',
    version='1.0.1',
    description='It is a simple horizontal accordion for django cms',
    long_description=open('README.rst').read(),
    author='Luisza',
    license = "GPLv2",
    author_email='luisza14@gmail.com',
    url='http://github.com/luisza/accordion_presentation',
    packages=find_packages(),
    keywords='tab django cms django-cms plugin',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').read().split('\n'),
)
