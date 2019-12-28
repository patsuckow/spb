import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


def find_requires():
    requirements = []
    dir_path = os.path.dirname(os.path.relpath(__file__))
    with open(f'{dir_path}requirements.txt') as f:
        requirements = f.readlines()

    return requirements


if __name__ == "__main__":
    ver = '0.1.0'

    setup(
        name='spb',
        version=ver,
        url='https://github.com/patsuckow/spb',
        download_url=f'https://github.com/patsuckow/spb/arhive/{ver}.tar.gz',
        description='Simple Progress Bar',
        long_description=long_description,
        long_description_content_type="text/markdown",
        keywords=[
            'progress',
            'progress bar',
            'progressbar',
            'progress indicator',
            'percent indicator',
            'timer indicator',
            'data rate indicator',
            'transmitted data indicator',
            'console progress',
            'bar'

        ],
        license='GNU General Public License v3 (GPLv3)',
        author='Alexey Patsukov 🇷🇺',
        author_email='patsuckow@yandex.ru',
        packages=find_packages(exclude=[
            '*.tests', '*.tests.*', 'tests',
            '*.examples', '*.examples.*', 'examples',
            '*..github', '*..github.*', '.github'
        ]),
        include_package_data=True,
        zip_safe=False,
        install_requires=find_requires(),
        setup_requires=[],
        test_suite='tests',
        classifiers=[
            # As in https://pypi.python.org/pypi?:action=list_classifiers
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Operating System :: OS Independent',
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            "Topic :: Software Development :: Libraries",
            'Topic :: Utilities',
        ],
        python_requires='>=3.6',
    )
