from setuptools import setup
from setuptools import find_packages


setup(
    name='foolscap',
    version='0.3.1',
    author='S. Williams-Wynn',
    author_email='s.williamswynn.mail@gmail.com',
    packages=find_packages(
        include=['foolscap', 'foolscap.*'],
        exclude=['tests'],
    ),
    entry_points={
        'console_scripts': [
            'fscap=foolscap.cli:main',
        ]
    },
    install_requires=["vim-edit"],
    classifiers=[
        "Environment :: Console",
        "Operation System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
