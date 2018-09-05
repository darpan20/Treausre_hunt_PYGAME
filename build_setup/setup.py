from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
print(PYTHON_INSTALL_DIR)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
setup(
        name = "Treasure Hunt",
        version = "0.1",

        description = "Treasure Game",
        options={"build_exe":{"packages":["pygame","sys","os","ctypes","random"],"include_files":["Treasure Hunt.py","D:\\final\\jjj.jpg","D:\\final\\tre1.jpg","D:\\final\\pl.png","D:\\final\\pn1.png","D:\\final\\tip.png","D:\\final\\th.png","D:\\final\\home.png","D:\\final\\NEXT.png","D:\\final\\round1.png","D:\\final\\r.png","D:\\final\\21.gif","D:\\final\\round3.png","D:\\final\\spritesheet (1).png","D:\\final\\go.png","D:\\final\\sl.png","D:\\final\\br.png","D:\\final\\123.png","D:\\final\\download (2).png","D:\\final\\spritesheet.png","D:\\final\\1.jpg","D:\\final\\startmusic.wav","D:\\final\\mainmusic.wav","D:\\final\\topen.wav","D:\\final\\tclose.wav","D:\\final\\click.wav","D:\\final\\coins.png",os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')],"excludes":['adodbapi', 'alabaster', 'asn1crypto', 'asyncio', 'attr', 'babel', 'backcall', 'backports', 'bokeh', 'botocore', 'bottleneck', 'bs4', 'certifi', 'cffi', 'chardet', 'click', 'cloudpickle', 'colorama', 'concurrent', 'cryptography', 'curses', 'Cython', 'cytoolz', 'dask', 'dateutil', 'distributed', 'distutils', 'docutils', 'email', 'et_xmlfile', 'h5py', 'html', 'html5lib', 'http', 'idna', 'ipykernel', 'IPython', 'ipython_genutils', 'ipywidgets', 'jedi', 'jinja2', 'json', 'jsonschema', 'jupyter_client', 'jupyter_core', 'lib2to3', 'locket', 'logging', 'lxml', 'markupsafe', 'matplotlib', 'mkl_random', 'more_itertools', 'msgpack', 'multiprocessing', 'nbconvert', 'nbformat', 'nose', 'notebook', 'numexpr', 'numpy', 'numpydoc', 'openpyxl', 'OpenSSL', 'packaging', 'pandas', 'parso', 'partd', 'pathlib2', 'patsy', 'PIL', 'pkg_resources', 'pluggy', 'prompt_toolkit', 'psutil', 'py', 'pyasn1', 'pycparser', 'pydoc_data', 'pygments', 'PyQt5', 'pytz', 'pywin', 'pyximport', 'qtpy', 'requests', 'scipy', 'setuptools', 'sklearn', 'sortedcontainers', 'sphinx', 'sphinxcontrib', 'sqlalchemy', 'sqlite3', 'statsmodels', 'tables', 'tblib', 'test','tkinter', 'testpath', 'toolz', 'tornado', 'traitlets', 'unittest', 'urllib', 'urllib3', 'wcwidth', 'webencodings', 'win32com', 'win_unicode_console', 'xlrd', 'xlsxwriter', 'xlwt', 'xml', 'xmlrpc', 'yaml', 'zict', 'zmq', '_pytest']}},
        executables = [Executable(script="Treasure Hunt.py",icon="D:\\final\\tlogo.ico")]
)
