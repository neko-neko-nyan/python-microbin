import sys
import inspect
import os


sys.path.insert(0, os.path.abspath('..'))


project = 'MicroBIN python'
author = 'NekoNekoNyan'
copyright = '2023, NekoNekoNyan'

root_doc = 'index'
language = 'en'
html_theme = "sphinx_rtd_theme"
tls_verify = False

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    # 'sphinxcontrib.fulltoc',
    'sphinx_mdinclude',
]

autodoc_member_order = 'bysource'
autodoc_typehints_format = 'fully-qualified'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}


def linkcode_resolve(domain, info):
    def find_source():
        # try to find the file and line number, based on code from numpy:
        # https://github.com/numpy/numpy/blob/master/doc/source/conf.py#L286
        obj = sys.modules[info['module']]
        for part in info['fullname'].split('.'):
            obj = getattr(obj, part)
        fn = inspect.getsourcefile(obj)
        fn = os.path.relpath(fn, start=os.path.abspath('.'))
        source, lineno = inspect.getsourcelines(obj)
        return fn, lineno, lineno + len(source) - 1

    if domain != 'py' or not info['module']:
        return None
    try:
        filename = '%s#L%d-L%d' % find_source()
    except Exception:
        filename = info['module'].replace('.', '/') + '.py'
    import subprocess
    # tag = subprocess.Popen(['git', 'rev-parse', 'HEAD'],
    #                        stdout=subprocess.PIPE,
    #                        universal_newlines=True).communicate()[0][:-1]
    # https://github.com/runawayhorse001/statspy/blob/master/statspy/basics.py
    # https://github.com/runawayhorse001/SphinxGithub/blob/master/statspy/basics.py
    return "https://github.com/neko-neko-nyan/python-microbin/blob/main/%s" % (filename)
