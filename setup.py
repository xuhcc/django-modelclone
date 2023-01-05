from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = "django-modelclone-next",
    version = "0.8.2",
    description = "Django application that allows users to clone a model in Admin",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = "https://github.com/xuhcc/django-modelclone",
    packages = [
        'modelclone',
    ],
    package_data = {
        'modelclone': ['templates/modelclone/*'],
    },
    author = "xuhcc",
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='MIT',
)
