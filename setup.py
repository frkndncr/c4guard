from setuptools import setup, find_packages

setup(
    name='C4Guard',
    version='0.1.0',
    description='A web application for searching files and monitoring system resources.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/frkndncr/c4guard',
    packages=find_packages(),
    install_requires=[
        'Flask>=1.1.2',
        'aiohttp>=3.7.4',
        'beautifulsoup4>=4.9.3',
        'numpy>=1.19.5',
        'aiohappyeyeballs>=1.0.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
