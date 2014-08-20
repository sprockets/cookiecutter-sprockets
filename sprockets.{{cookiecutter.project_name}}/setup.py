import codecs
import sys

import setuptools

from sprockets.{{cookiecutter.project_name}} import __version__


def read_requirements_file(req_name):
    requirements = []
    try:
        with codecs.open(req_name, encoding='utf-8') as req_file:
            for req_line in req_file:
                if '#' in req_line:
                    req_line = req_line[0:req_line.find('#')].strip()
                if req_line:
                    requirements.append(req_line.strip())
    except IOError:
        pass
    return requirements


install_requires = read_requirements_file('requirements.txt')
setup_requires = read_requirements_file('setup-requirements.txt')
tests_require = read_requirements_file('test-requirements.txt')

if sys.version_info < (2, 7):
    install_requires.append('argparse')
    install_requires.append('logutils')
    tests_require.append('unittest2')
if sys.version_info < (3, 0):
    tests_require.append('mock')

setuptools.setup(
    name='sprockets.{{cookiecutter.project_name}}',
    version=__version__,
    description='{{cookiecutter.description}}',
    long_description=codecs.open('README.rst', encoding='utf-8').read(),
    url='https://github.com/{{cookiecutter.git_org}}/sprockets.{{cookiecutter.project_name}}.git',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license=codecs.open('LICENSE', encoding='utf-8').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=setuptools.find_packages(
        exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    namespace_packages=['sprockets'],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    zip_safe=True,
)
