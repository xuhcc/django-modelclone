from distutils.core import setup
from os.path import dirname, join

setup(
    name = "django-modelclone-next",
    version = "0.8.0",
    description = "Django application that allows users to clone a model in Admin",
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
