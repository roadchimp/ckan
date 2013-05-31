''' This file is intended to hold util functions that can be used anywhere
in ckan.  We do not want to import any part of ckan into this file as that
will end up leading to circular imports. '''

import re

def version_str_2_list(v_str):
    ''' convert a version string into a list of ints
    eg 1.6.1b --> [1, 6, 1] '''
    v_str = re.sub(r'[^0-9.]', '', v_str)
    return [int(part) for part in v_str.split('.')]
