from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
# from distutils.core import setup
import os

long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')
                        ).read()

setup(
    name='lcd2usb',
    description=next(x for x in long_description.splitlines() if x.strip()),
    #description=long_description.split('\n')[0],
    long_description='.. contents::\n\n' + str(long_description, encoding='utf-8'),
    keywords='usb lcd lcd2usb',
    version='1.0',
    author='Xie Yanbo',
    author_email='xieyanbo@gmail.com',
    url='http://github.com/xyb/lib2usb',
    license='New BSD',
    platforms=['any'],
    py_modules=['lcd2usb'],
    install_requires=['libusb1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware :: Hardware Drivers',
    ],
)
