from setuptools import setup, find_packages

setup(
  name='err-backend-slackv3',
  version='0.1.0',
  packages=[*find_packages(), '.'],
  description="Slack(v3) backend for Errbot"
)
