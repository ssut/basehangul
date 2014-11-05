# -*- coding: utf-8 -*-
import array
import sys
import binascii

PY3 = sys.version_info >= (3, 0)
# padding character '흐'
if PY3:
    PADDING = chr(0xD750)
else:
    PADDING = unichr(0xD750)

def encode(data):
    chunks = str2chunks(asc2bin(data), 10)
    padding = ''
    last = chunks[-1]
    if last:
        size = len(last)
        if size == 2:
            chunks[-1] = '1%s' % (last.rjust(10, '0'))
        elif size in (4, 6, 8):
            padding = PADDING * (size / 2 - 1)

    result = [bin2hangul(int(b.ljust(10, '0'), 2)) for b in chunks]
    result.append(padding)
    return ''.join(result)

def decode(data):
    indexes = [hangul2bin(c) for c in data]
    binaries = []
    for index in indexes:
        char = ''
        if index == -1:
            pass
        elif 0 <= index <= 1023:
            char = bin(index)[2:].zfill(10)
        elif 1024 <= index <= 1027:
            char = bin(index - 1024)[2:].zfill(2)
        binaries.append(char)
    binary = ''.join(binaries)
    size = len(binary)
    cut = -(size % 8 + 1)
    if cut != -1:
        binary = binary[0:cut]
    return binascii.unhexlify('%x' % int(binary, 2)).decode('utf-8')

def asc2bin(data):
    result = ''
    binaries = []
    for char in data:
        char = format(ord(char), 'b').zfill(8)
        binaries.append(char)
    return ''.join(binaries)


def str2chunks(data, size):
    if size <= 0:
        raise ValueError('Invalid slice size')
    array = [data[i:i+size] for i in range(0, len(data), size)]
    return array

def bin2hangul(index):
    if index < 0 or index > 1027:
        raise IndexError('Index {} outside of valid range: 0..1027'.format(
            index))

    hangul = array.array('B')
    key = int(int(index / 0x5E) * 0x100 + index % 0x5E + 0xB0A1)
    hx = hex(key)
    for i in range(2, len(hx) - 1, 2):
        hangul.append(int(hx[i:i+2], 16))
    hangul = hangul.tostring().decode('euc-kr')
    return hangul

def hangul2bin(hangul):
    if hangul == PADDING:
        return -1
    offset = int(binascii.hexlify(hangul.encode('euc-kr')), 16) - 0xB0A1
    index = int(offset / 0x100) * 0x5E + offset % 0x100
    if index < 0 or index > 1027:
        raise ValueError('Not a valid BaseHangul string')
    return index
