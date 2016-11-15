# -*- coding: utf-8 -*-
"""
Overridable settings.
"""
import os

try:
    from .base import *  # NOQA
except ImportError:
    pass

env = os.environ.get("ENV", 'development')
print('Environment: {}'.format(env))

try:
    m = __import__(
        '{{ project_name }}.settings.environment_overrides.{}'.format(env),
        globals=globals(), locals=locals(), fromlist="*"
    )
    try:
        attrlist = m.__all__
    except AttributeError:
        attrlist = dir(m)
    for attr in [a for a in attrlist if '__' not in a]:
        globals()[attr] = getattr(m, attr)
except ImportError:
    print('Environment override not found for {}.'.format(env))
    pass
