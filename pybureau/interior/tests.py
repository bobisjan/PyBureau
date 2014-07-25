from __future__ import unicode_literals

import unittest

from . import CardValidator
from .exceptions import InvalidCardError, InvalidFormatCardError


class CardValidationTestCase(unittest.TestCase):

    def test_invalid_arguments(self):
        self.assertRaises(TypeError, CardValidator.validate)
        self.assertRaises(InvalidFormatCardError, CardValidator.validate, None)
        self.assertRaises(InvalidFormatCardError, CardValidator.validate, '')
        self.assertRaises(InvalidFormatCardError, CardValidator.validate, 'ZC0e0655')
        self.assertRaises(InvalidCardError, CardValidator.validate, '1234')


if __name__ == '__main__':
    unittest.main()
