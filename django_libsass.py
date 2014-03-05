from django.contrib.staticfiles.finders import get_finders

import sass
from compressor.filters.base import FilterBase

def get_include_paths():
    """
    Generate a list of include paths that libsass should use to find files
    mentioned in @import lines.
    """
    include_paths = []

    # Look for staticfile finders that define 'storages'
    for finder in get_finders():
        try:
            storages = finder.storages
        except AttributeError:
            continue

        for storage in storages.itervalues():
            try:
                include_paths.append(storage.path('.'))
            except NotImplementedError:
                # storages that do not implement 'path' do not store files locally,
                # and thus cannot provide an include path
                pass

    return include_paths


INCLUDE_PATHS = None  # populate this on first call to 'compile'

def compile(**kwargs):
    """Perform sass.compile, but with the appropriate include_paths for Django added"""
    global INCLUDE_PATHS
    if INCLUDE_PATHS is None:
        INCLUDE_PATHS = get_include_paths()

    kwargs = kwargs.copy()
    kwargs['include_paths'] = (kwargs.get('include_paths') or []) + INCLUDE_PATHS
    return sass.compile(**kwargs)


class SassCompiler(FilterBase):
    def __init__(self, content, attrs=None, filter_type=None, filename=None):
        # FilterBase doesn't handle being passed attrs, so fiddle the signature
        super(SassCompiler, self).__init__(content, filter_type, filename)

    def input(self, **kwargs):
        if self.filename:
            return compile(filename=self.filename)
        else:
            return compile(string=self.content)
