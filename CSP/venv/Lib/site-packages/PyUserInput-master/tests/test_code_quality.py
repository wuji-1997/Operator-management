import unittest
import pycodestyle
import os
import os.path
import itertools


class TestCodeFormat(unittest.TestCase):
    def test_conformance(self):
        """Test that we conform to PEP-8."""
        ignore_these_for_now = ['E111',
                                'E116',
                                'E121',
                                'E123',
                                'E126',
                                'E127',
                                'E128',
                                'E203',
                                'E225',
                                'E226',
                                'E231',
                                'E251',
                                'E261',
                                'E265',
                                'E266',
                                'E301',
                                'E302',
                                'E303',
                                'E305',
                                'E501',
                                'W391',
                                'W292',
                                'W293']
        style = pycodestyle.StyleGuide(quiet=False, ignore=ignore_these_for_now)

        style.input_dir('.')
        result = style.check_files()
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
