from setuptools import setup, find_packages
from django_restapi import __version__

PACKAGES=find_packages('.')
REQUIRES=['django']

setup(name = "django-restapi-op",
      version = __version__,
      author = "Naranjo Manuel Francisco",
      author_email = "manuel@aircable.net",
      description = ("Django REST API modified for OpenProximity"),
      license = "Apache V2",
      packages = PACKAGES,
      url = "https://github.com/OpenProximity/django_restapi",
      include_package_data = True,
      
      install_requires = REQUIRES,
      zip_safe = False,
)
