from setuptools import setup, find_packages

setup(
    name='d',
    version='0.1.0',
    description='A pipwin alternative that installs prebuilt wheels from PyPI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/pipwind',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'pipwind=pipwind.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
