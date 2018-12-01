'''
Image files.
'''

import os.path

__all__ = 'image',


def image(filename: str or tuple) -> str:
    '''
    Return full path to image file.

    Args:
        file: basename of image file
    Returns:
        str: full path to image file
    '''

    imagedir = os.path.join(os.path.dirname(__file__), '../images')
    is_str = isinstance(filename, str)
    fname = filename if is_str else filename[0]
    imagepath = os.path.join(imagedir, '{0:s}.png'.format(fname))
    return os.path.normpath(imagepath), None if is_str else filename[1]
