# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name='django-gst-field',
    version='0.0.2',
    url='https://github.com/jinchuuriki91/django-gst-field',
    license='MIT',
    platforms=['OS Independent'],
    description="GST and PAN number field for django models.",
    install_requires=[
        'Django>=1.11.20'
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Gandhar Pednekar',
    author_email='gandhar.pednekar15@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='django orm python',
)
