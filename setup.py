# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016, 2017 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Crawler integration with INSPIRE-HEP."""

from __future__ import absolute_import, print_function

from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'mock~=2.0,>=2.0.0',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
    'requests_mock~=1.0,>=1.4.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.5,<1.6',
    ],
    'postgresql': [
        'invenio-db[postgresql,versioning]==1.0.0',
    ],
    'mysql': [
        'invenio-db[mysql,versioning]==1.0.0',
    ],
    'sqlite': [
        'invenio-db[versioning]==1.0.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'autosemver~=0.2,>=0.2',
    'Babel>=1.3',
    'pytest-runner>=2.6.2',
]

install_requires = [
    'autosemver~=0.2,>=0.2',
    'six>=1.9.0',
    'Flask>=0.12.2',
    'python-scrapyd-api>=2.0.1',
    'pathlib2>=2.1.0',
    'invenio-celery>=1.0.0a3',
    'celery~=4.0,>=4.1.0',
    'invenio_workflows~=7.0',
    'invenio_workflows_ui~=2.0.1',
    'invenio_oaiharvester>=1.0.0a3',
]

packages = find_packages()
URL = 'https://github.com/inspirehep/inspire-crawler'


setup(
    name='inspire-crawler',
    autosemver={
        'bugtracker_url': URL + '/issues/'
    },
    description=__doc__,
    long_description=readme,
    keywords='invenio inspire scrapy crawler',
    license='GPLv2',
    author='CERN',
    author_email='feedback@inspirehep.net',
    url=URL,
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.api_apps': [
            'inspire_crawler = inspire_crawler:INSPIRECrawler',
        ],
        'invenio_base.apps': [
            'inspire_crawler = inspire_crawler:INSPIRECrawler',
        ],
        'invenio_db.alembic': [
            'inspire_crawler = inspire_crawler:alembic',
        ],
        'invenio_db.models': [
            'inspire_crawler = inspire_crawler.models',
        ],
        'invenio_celery.tasks': [
            'inspire_crawler = inspire_crawler.tasks',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 1 - Planning',
    ],
)
