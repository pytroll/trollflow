#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Unit testing for utils
"""

import unittest
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from threading import RLock

from trollflow import utils


class TestUtils(unittest.TestCase):

    yaml_config = """config:
    item_1: 1
    item_2: 2
    """

    lock = RLock()

    def test_get_class(self):
        res = utils.get_class("trollflow.utils")
        self.assertTrue(res == utils)

    def test_ordered_load(self):
        fid = StringIO(self.yaml_config)
        res = utils.ordered_load(fid)
        fid.close()
        self.assertTrue(res.keys()[0] == "config")
        keys = res["config"].keys()
        self.assertTrue(keys[0] == "item_1")
        self.assertTrue(res["config"][keys[0]] == 1)
        self.assertTrue(keys[1] == "item_2")
        self.assertTrue(res["config"][keys[1]] == 2)

    def test_acquire_lock(self):
        self.assertEqual(self.lock._RLock__count, 0)
        utils.acquire_lock(self.lock)
        self.assertEqual(self.lock._RLock__count, 1)

    def test_release_lock(self):
        self.assertEqual(self.lock._RLock__count, 1)
        utils.release_lock(self.lock)
        self.assertEqual(self.lock._RLock__count, 0)


def suite():
    """The suite for test_global_mosaic
    """
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestUtils))

    return mysuite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
