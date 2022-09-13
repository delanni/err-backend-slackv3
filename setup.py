from setuptools import setup, find_packages

setup(
  name='err-backend-slackv3',
  version='0.1.0',

  # Use one of the below approach to define package and/or module names:

  # this approach automatically finds out all directories (packages) - those must contain a file named __init__.py (can be empty)
  packages=find_packages(),

  description="Slack(v3) backend for Errbot"
)
