modules_list = ['__future__', '__hello__', '__main__', '__phello__', '_abc', '_aix_support', '_android_support', '_apple_support', '_ast', '_asyncio', '_bisect',
                '_blake2', '_bz2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections',
                '_collections_abc', '_colorize', '_compat_pickle', '_compression', '_contextvars', '_csv', '_ctypes', '_ctypes_test', '_datetime', '_decimal',
                '_elementtree', '_functools', '_hashlib', '_heapq', '_imp', '_interpchannels', '_interpqueues', '_interpreters', '_io', '_ios_support', '_json',
                '_locale', '_lsprof', '_lzma', '_markupbase', '_md5', '_multibytecodec', '_multiprocessing', '_opcode', '_opcode_metadata', '_operator',
                '_osx_support', '_overlapped', '_pickle', '_py_abc', '_pydatetime', '_pydecimal', '_pyio', '_pylong', '_pyrepl', '_queue', '_random', '_sha1',
                '_sha2', '_sha3', '_signal', '_sitebuiltins', '_socket', '_sqlite3', '_sre', '_ssl', '_stat', '_statistics', '_string', '_strptime', '_struct',
                '_suggestions', '_symtable', '_sysconfig', '_testbuffer', '_testcapi', '_testclinic', '_testclinic_limited', '_testconsole', '_testimportmultiple',
                '_testinternalcapi', '_testlimitedcapi', '_testmultiphase', '_testsinglephase', '_thread', '_threading_local', '_tkinter', '_tokenize',
                '_tracemalloc', '_typing', '_uuid', '_warnings', '_weakref', '_weakrefset', '_winapi', '_wmi', '_zoneinfo', 'abc', 'antigravity', 'argparse',
                'array', 'ast', 'asyncio', 'atexit', 'autocomplete', 'autocomplete_w', 'autoexpand', 'base64', 'bdb', 'binascii', 'bisect', 'browser', 'builtins',
                'bz2', 'cProfile', 'calendar', 'calltip', 'calltip_w', 'cmath', 'cmd', 'code', 'codecontext', 'codecs', 'codeop', 'collections', 'colorizer',
                'colorsys', 'compileall', 'concurrent', 'config', 'config_key', 'configdialog', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg',
                'csv', 'ctypes', 'curses', 'dataclasses', 'datetime', 'dbm', 'debugger', 'debugger_r', 'debugobj', 'debugobj_r', 'decimal', 'delegator', 'difflib',
                'dis', 'doctest', 'dynoption', 'editor', 'email', 'encodings', 'ensurepip', 'enum', 'errno', 'faulthandler', 'filecmp', 'fileinput', 'filelist',
                'fnmatch', 'format', 'fractions', 'ftplib', 'functools', 'gc', 'genericpath', 'getopt', 'getpass', 'gettext', 'glob', 'graphlib', 'grep', 'gzip',
                'hashlib', 'heapq', 'help', 'help_about', 'history', 'hmac', 'html', 'http', 'hyperparser', 'idle', 'idle_test', 'idlelib', 'imaplib', 'importlib',
                'inspect', 'io', 'iomenu', 'ipaddress', 'itertools', 'json', 'keyword', 'linecache', 'locale', 'logging', 'lzma', 'macosx', 'mailbox', 'mainmenu',
                'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'msvcrt', 'multicall', 'multiprocessing', 'netrc', 'nt', 'ntpath', 'nturl2path', 'numbers',
                'opcode', 'operator', 'optparse', 'os', 'outwin', 'parenmatch', 'pathbrowser', 'pathlib', 'pdb', 'percolator', 'pickle', 'pickletools', 'pip',
                'pkgutil', 'platform', 'plistlib', 'poplib', 'posixpath', 'pprint', 'profile', 'pstats', 'pty', 'py_compile', 'pyclbr', 'pydoc', 'pydoc_data',
                'pyexpat', 'pygame', 'pyparse', 'pyshell', 'query', 'queue', 'quopri', 'random', 're', 'redirector', 'replace', 'reprlib', 'rlcompleter', 'rpc',
                'run', 'runpy', 'runscript', 'sched', 'scrolledlist', 'search', 'searchbase', 'searchengine', 'secrets', 'select', 'selectors', 'shelve', 'shlex',
                'shutil', 'sidebar', 'signal', 'site', 'smtplib', 'socket', 'socketserver', 'sqlite3', 'squeezer', 'sre_compile', 'sre_constants', 'sre_parse', 'ssl',
                'stackviewer', 'stat', 'statistics', 'statusbar', 'string', 'stringprep', 'struct', 'subprocess', 'symtable', 'sys', 'sysconfig', 'tabnanny',
                'tarfile', 'tempfile', 'test', 'textview', 'textwrap', 'this', 'threading', 'time', 'timeit', 'tkinter', 'token', 'tokenize', 'tomllib', 'tooltip',
                'trace', 'traceback', 'tracemalloc', 'tree', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'undo', 'unicodedata', 'unittest', 'urllib', 'util',
                'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'window', 'winreg', 'winsound', 'wsgiref', 'xml', 'xmlrpc', 'xxsubtype', 'zipapp',
                'zipfile', 'zipimport', 'zlib', 'zoneinfo', 'zoomheight', 'zzdummy']
def check_in(module):
    return module in modules_list

isin = check_in(input('What module do you want to find? -'))
if isin:
    print('It\'s there all right!')
else:
    print('Not in... you may have to install!')

'''
IT TOOK ME 30 MIN TO PARSE THE TEXT FROM THE HELP INTERACTIVE
INTO THIS LIST
PLEASE HANDLE WITH CARE
'''