import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'))
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="py-eve-intel-client",
    version="0.1",
    author="Andrew Martinez",
    author_email="andrew.p.martinez@gmail.com",
    install_requires=[
        reqs
    ],
    description=("A client for reporting intel from an EVE Online chat log to an instance of py-eve-intel-server."),
    license="MIT",
    keywords="EVE chat monitor intel client",
    url='https://github.com/andrewpmartinez/py-eve-intel-client',
    download_url='https://github.com/andrewpmartinez/py-eve-chat-client/tarball/0.1',
    packages=find_packages(),
    long_description="See github page for full details.",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only'
    ],
)
