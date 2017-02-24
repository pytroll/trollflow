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

"""Unit testing for WorkflowStreamer
"""

import unittest
from mock import patch
import StringIO

from trollflow.workflow_streamer import WorkflowStreamer


class TestWorkflowStreamer(unittest.TestCase):

    streamer = None
    config_str = """"""
    config = StringIO.StringIO(config_str)

    @patch("trollflow.workflow_streamer.workflow_runner")
    def test_init(self, runner):
        self.streamer = WorkflowStreamer(config=self.config)
        self.assertIsNotNone(self.streamer.workflow)
        self.assertIsNone(self.input_queue)
        self.assertTrue(hasattr(self.output_queue, 'get'))
        self.assertIsNone(self.prev_lock)
        self.assertIsNone(self.lock)


def suite():
    """The suite for test_workflow_streamer
    """
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestWorkflowStreamer))

    return mysuite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
