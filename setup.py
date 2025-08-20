# -*- coding: utf-8 -*-
"""Installer for the eteaching.plone.dataspaceconnector package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGELOG.md").read(),
    ]
)


setup(
    name='eteaching.plone.dataspaceconnector',
    version='1.0b2',
    description="Add on to connect the data room of MeinBildungsraum to Plone",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.1",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Markus Schmidt',
    author_email='m.schmidt@iwm-tuebingen.de',
    url='https://github.com/e-teachingorg/eteaching.plone.dataspaceconnector',
    project_urls={
        'Source': 'https://github.com/collective/eteaching.plone.openbadges',
        'Tracker': 'https://github.com/collective/eteaching.plone.openbadges/issues',
        # 'Documentation': 'https://eteaching.plone.dataspaceconnector.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['eteaching', 'eteaching.plone'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'z3c.jbot',
        'plone.api>=1.8.4',
        'plone.app.dexterity',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = eteaching.plone.dataspaceconnector.locales.update:update_locale
    """,
)
