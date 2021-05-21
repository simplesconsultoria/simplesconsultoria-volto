# -*- coding: utf-8 -*-
"""Installer for the simplesconsultoria.volto package."""

from setuptools import find_packages, setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="simplesconsultoria.volto",
    version="1.0a1",
    description="Portal Policy for Simples Consultoria web site",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Simples Consultoria",
    author_email="dev@simplesconsultoria.com.br",
    url="https://github.com/simplesconsultoria/simplesconsultoria-volto",
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/simplesconsultoria.volto",
        "Source": "https://github.com/simplesconsultoria/simplesconsultoria-volto",
        "Tracker": "https://github.com/simplesconsultoria/simplesconsultoria-volto/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["simplesconsultoria"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
        "collective.folderishtypes",
        "plone.api",
        "plone.restapi",
        "plone.app.dexterity",
    ],
    extras_require={
        "test": [
            "towncrier",
            "zestreleaser.towncrier",
            "zest.releaser[recommended]",
            "plone.app.testing",
            "plone.testing",
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = simplesconsultoria.volto.locales.update:update_locale
    """,
)
