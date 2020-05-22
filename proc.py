#!/usr/bin/env python
# coding: utf-8

import errno
import io
import logging
import os
import pty
import select
import subprocess
import sys

logger = logging.getLogger(__name__)

defenc = None

if hasattr(sys, 'getfilesystemencoding'):
    defenc = sys.getfilesystemencoding()

if defenc is None:
    defenc = sys.getdefaultencoding()


