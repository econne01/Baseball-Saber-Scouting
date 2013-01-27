from setuptools import setup, find_packages

setup(
    name = "baseball_saber_scouting",
    version = "0.1",
    url = 'http://github.com/econne01/baseball-saber-scouting',
    description = "A Django app for retrieving baseball data and viewing statistic scouting reports",
    author = 'Eric Connelly',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)