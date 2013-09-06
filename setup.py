#!/usr/bin/env python2.7
# Copyright 2008-2013 semantics GmbH
# Written by Christian Heimes <c.heimes@semantics.de>
# Modified by Marcus Brinkmann <m.brinkmann@semantics.de>

try:
    import setuptools
except ImportError:
    from distutils.core import setup
else:
    from setuptools import setup

setup_info = dict(
    name="smc.mw",
    version="0.1",
    packages=["smc.mw"],
    namespace_packages=["smc"],
    zip_safe=True,
    requires=["lxml", "grako"],
    entry_points = {
        'console_scripts': [
            'mw = smc.mw.tool:main',
        ]
    },
    author="semantics GmbH / Marcus Brinkmann",
    author_email="m.brinkmann@semantics.de",
    maintainer="Marcus Brinkmann",
    maintainer_email="m.brinkmann@semantics.de",
    url="https://github.com/lambdafu/smc.mw",
    keywords="wiki mediawiki parser peg",
    license="BSD",
    description="MediaWiki-compatible parser for Python.",
    long_description=open("README.mediawiki").read(),
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Topic :: Text Processing :: Markup",
    ),
)

setup(**setup_info)