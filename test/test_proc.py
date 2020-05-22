import os
import sys
import time
import unittest

import pk3proc
import pk3ut

dd = pk3ut.dd

this_base = os.path.dirname(__file__)


class TestProcError(unittest.TestCase):

    foo_fn = '/tmp/foo'

    def _clean(self):

        # remove written file
        try:
            os.unlink(self.foo_fn)
        except EnvironmentError:
            pass

    def setUp(self):
        self._clean()

    def tearDown(self):
        self._clean()

    def test_procerror(self):
        inp = (1, 'out', 'err', ['ls', 'a', 'b'], {"close_fds": True})
        ex_args = (1, 'out', 'err', ['out'], ['err'],  ['ls', 'a', 'b'], {"close_fds": True})
        ex = pk3proc.CalledProcessError(*inp)

        self.assertEqual(ex_args, (ex.returncode,
                                   ex.stdout,
                                   ex.stderr,
                                   ex.out,
                                   ex.err,
                                   ex.cmd,
                                   ex.options))

        self.assertEqual(inp, ex.args)
