#
# Copyright (C) 2020 Arm Mbed. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
from mbed_tools_lib import __version__
from unittest import TestCase


class TestPackage(TestCase):
    def test_version(self):
        self.assertIsNotNone(__version__)
