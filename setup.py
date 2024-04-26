from setuptools import setup, find_packages

setup(
    name='password-checker-app',
    version='1.0.0',
    author='Zhenya Vardanyan',
    author_email='zhenya.vardanyan6@gmail.com',
    description='Web app for checking and generating passwords',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zhensvans/password-checker-app',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
