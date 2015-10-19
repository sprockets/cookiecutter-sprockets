from sprockets.{{cookiecutter.project_name}} import version_info, __version__

needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
]
templates_path = []
source_suffix = '.rst'
master_doc = 'index'
project = 'sprockets.{{cookiecutter.project_name}}'
copyright = '{{cookiecutter.year}}, {{cookiecutter.full_name}}'
version = '.'.join(__version__.split('.')[0:1])
release = __version__
if len(version_info) > 3:
    release += '-{0}'.format(str(v) for v in version_info[3:])
exclude_patterns = []
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sprockets': ('https://sprockets.readthedocs.org/en/latest/', None),
}
