from setuptools import setup, find_packages

setup(
    name='yangsrunner',
    version='0.1.0',
    description='Terminal Application Runner',
    long_description='Terminal Application Runner',
    keywords=['terminal'],
    license='MIT',
    python_requires='>=3.5',
    author='seiren87',
    author_email='seiren87dev@gmail.com',
    url='https://github.com/seiren87/yangsrunner',
    install_requires=[
        'yangsutil==0.1.0'
    ],
    packages=find_packages(
        exclude=['test*']
    ),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'yangsrunner=yangsrunner.run:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
