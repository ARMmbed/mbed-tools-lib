from unittest import TestCase
from mbed_tools_lib.config_option import ConfigOption


class TestConfigOption(TestCase):
    def test_is_hashable(self):
        name = "foo"
        doc = "documentation"

        options = set([ConfigOption(name=name, doc=doc), ConfigOption(name=name, doc=doc)])

        assert len(options) == 1
