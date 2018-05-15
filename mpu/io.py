#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Reading and writing common file formats."""

from __future__ import absolute_import

# core modules
import csv
import json
import os
# Make it work for Python 2+3 and with Unicode
import io as io_stl
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# internal modules
from mpu.datastructures import EList


def read(filepath, **kwargs):
    """
    Read a file.

    Supported formats:

    * CSV
    * JSON

    Parameters
    ----------
    filepath : str
        Path to the file that should be read. This methods action depends
        mainly on the file extension.
    kwargs : dict
        Any keywords for the specific file format.

    Returns
    -------
    data : str or bytes
    """
    if filepath.lower().endswith('.csv'):
        with open(filepath, 'r') as fp:
            if 'delimiter' not in kwargs:
                kwargs['delimiter'] = ','
            if 'quotechar' not in kwargs:
                kwargs['quotechar'] = '"'
            if 'skiprows' not in kwargs:
                kwargs['skiprows'] = []
            if isinstance(kwargs['skiprows'], int):
                kwargs['skiprows'] = [i for i in range(kwargs['skiprows'])]
            skiprows = kwargs['skiprows']
            kwargs.pop('skiprows', None)
            reader = csv.reader(fp, **kwargs)
            data = EList([row for row in reader])
            data = data.remove_indices(skiprows)
        return data
    elif filepath.lower().endswith('.json'):
        with open(filepath) as data_file:
            data = json.load(data_file, **kwargs)
        return data
    else:
        raise NotImplementedError('File \'{}\' is not known.'.format(filepath))


def write(filepath, data, **kwargs):
    """
    Write a file.

    Supported formats:

    * CSV
    * JSON

    Parameters
    ----------
    filepath : str
        Path to the file that should be read. This methods action depends
        mainly on the file extension.
    data : dict or list
        Content that should be written
    kwargs : dict
        Any keywords for the specific file format.

    Returns
    -------
    data : str or bytes
    """
    if filepath.lower().endswith('.csv'):
        with open(filepath, 'r') as fp:
            if 'delimiter' not in kwargs:
                kwargs['delimiter'] = ','
            if 'quotechar' not in kwargs:
                kwargs['quotechar'] = '"'
            with open(filepath, 'w') as fp:
                writer = csv.writer(fp, **kwargs)
                writer.writerows(data)
        return data
    elif filepath.lower().endswith('.json'):
        with io_stl.open(filepath, 'w', encoding='utf8') as outfile:
            if 'indent' not in kwargs:
                kwargs['indent'] = 4
            if 'sort_keys' not in kwargs:
                kwargs['sort_keys'] = True
            if 'separators' not in kwargs:
                kwargs['separators'] = (',', ': ')
            if 'ensure_ascii' not in kwargs:
                kwargs['ensure_ascii'] = False
            str_ = json.dumps(data, **kwargs)
            outfile.write(to_unicode(str_))
    else:
        raise NotImplementedError('File \'{}\' is not known.'.format(filepath))


def download(source, sink=None):
    """
    Download a file.

    Parameters
    ----------
    source : str
        Where the file comes from. Some URL.
    sink : str or None (default: same filename in current directory)
        Where the file gets stored. Some filepath in the local file system.
    """
    try:
        from urllib.request import urlretrieve  # Python 3
    except ImportError:
        from urllib import urlretrieve  # Python 2
    if sink is None:
        sink = os.path.abspath(os.path.split(source)[1])
    urlretrieve(source, sink)
    return sink
