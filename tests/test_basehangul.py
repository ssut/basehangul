#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('..')
import basehangul

class test_BaseHangul(unittest.TestCase):
    TEXT_ORIGINAL = 'This is an encoded string'
    TEXT_ENCODED = '넥라똔먈늴멥갯놓궂뗐밸뮤뉴뗐뀄굡덜멂똑뚤'

    def setUp(self):
        pass

    def test_encode(self):
        encoded = basehangul.encode(self.TEXT_ORIGINAL)
        self.assertEqual(encoded, TEXT_ENCODED)

    def test_decode(self):
        decoded = basehangul.encode(self.TEXT_ENCODED)
        self.assertEqual(decoded, TEXT_ORIGINAL)

if __name__ == '__main__':
    unittest.main()
