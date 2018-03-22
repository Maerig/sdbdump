from setuptools import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="sdbdump",
    version="0.1.2",
    description="Import/export AWS SimpleDB databases from/to JSON files.",
    long_description="Import/export AWS SimpleDB databases from/to JSON files.",
    author='Jean-Loup Roussel-Clouet',
    author_email='maerig@gmail.com',
    license='MIT',
    install_requires=requirements,
    python_requires='>=3.6.*',
    packages=['sdbdump'],
    package_dir={
        'sdbdump': 'sdbdump'
    },
    scripts=['bin/sdbdump'],
    url="https://github.com/Maerig/sdbdump"
)
