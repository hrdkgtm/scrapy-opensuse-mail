# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'opensuse_mail_crawler',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = opensuse_mail.settings']},
    install_requires = [
        'bs4'
    ]
)
