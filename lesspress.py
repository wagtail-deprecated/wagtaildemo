from compressor.filters.base import CompilerFilter
from django.conf import settings
from django.core.cache import cache

import hashlib
import time
import re
import os.path

LESS_COMPILER_COMMAND = getattr(settings, 'LESS_COMPILER_COMMAND', 'lessc {infile} {outfile}')

def get_dependencies_from_file(filename, deps):
    with open(filename, 'r') as content_file:
        content = content_file.read()
    get_dependencies_from_string(content, filename, deps)

def get_dependencies_from_string(str, base_filename, deps):
    filenames = re.findall(r'\@import\s+\"([^"]+)\";', str)

    if not filenames:
        return []

    if not base_filename:
        raise Exception('@import declaration found in inline LESS code')

    base_dirname = os.path.dirname(base_filename)
    immediate_deps = [os.path.normpath(os.path.join(base_dirname, filename)) for filename in filenames]

    unseen_deps = [dep for dep in immediate_deps if dep not in deps]
    for dep in unseen_deps:
        deps.add(dep)

    for dep in unseen_deps:
        get_dependencies_from_file(dep, deps)

class LessCompiler(CompilerFilter):
    def __init__(self, content, html_attrs, *args, **kwargs):
        super(LessCompiler, self).__init__(content, command=LESS_COMPILER_COMMAND, *args, **kwargs)

    def input(self, **kwargs):
        content_hash = 'lesspress-' + hashlib.sha1(self.content.encode('utf8')).hexdigest()
        data = cache.get(content_hash)
        if data:
            # check that all dependencies are older than timestamp
            data_is_fresh = True
            for dep in data['dependencies']:
                try:
                    if os.path.getmtime(dep) >= data['timestamp']:
                        data_is_fresh = False
                        break
                except OSError:
                    data_is_fresh = False
                    break

            if data_is_fresh:
                return data['output']

        data = {
            'timestamp': time.time(),
            'dependencies': set(),
        }
        data['output'] = super(LessCompiler, self).input(**kwargs)
        get_dependencies_from_string(self.content, self.filename, data['dependencies'])

        cache.set(content_hash, data, settings.COMPRESS_REBUILD_TIMEOUT)
        return data['output']
