import re
import unittest
from pathlib import Path

import k3xxnamexx


class TestVersion(unittest.TestCase):
    def test_version_matches_pyproject(self):
        pyproject = (Path(__file__).parent.parent / "pyproject.toml").read_text()
        match = re.search(r'^version = "(.+)"$', pyproject, re.MULTILINE)
        want = match.group(1)

        self.assertEqual(want, k3xxnamexx.__version__)
