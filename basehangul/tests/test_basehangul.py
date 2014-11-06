#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unittest

sys.path.append('..')
import basehangul

class test_BaseHangul(unittest.TestCase):
    TEST_CASES = (
        ('This is an encoded string', u'넥라똔먈늴멥갯놓궂뗐밸뮤뉴뗐뀄굡덜멂똑뚤'),
        ('123ab', u'꺽먹꼍녜'),
        ('123d\x00', u'꺽먹꼐가'),
        ('1', u'꺽흐흐흐'),
        ('12', u'꺽먈흐흐'),
        ('123', u'꺽먹꺄흐'),
        ('123d', u'꺽먹꼐빎'),
        ('123e', u'꺽먹꼐빔'),
        ('123f', u'꺽먹꼐빕'),
        ('123g', u'꺽먹꼐빗'),
    )

    def setUp(self):
        pass

    def test_empty(self):
        encoded = basehangul.encode('')
        self.assertEqual(encoded, '')

    def test_encode(self):
        for enc, dec in self.TEST_CASES:
            encoded = basehangul.encode(enc)
            self.assertEqual(encoded, dec)

    def test_decode(self):
        for enc, dec in self.TEST_CASES:
            decoded = basehangul.decode(dec)
            self.assertEqual(decoded, enc)

    def test_multibyte(self):
        ITEMS = (
            ('가', u'가'),
            ('가나', u'가나'),
            ('가나다', u'가나다'),
            ('가나다라', u'가나다라'),
        )
        for asc, uni in ITEMS:
            encoded = basehangul.encode(asc)
            decoded = basehangul.decode(encoded)
            self.assertEqual(decoded, uni)

if __name__ == '__main__':
    unittest.main()
