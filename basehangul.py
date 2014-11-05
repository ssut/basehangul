# -*- coding: utf-8 -*-

# padding character '흐'
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

def decode():
    pass

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

    hangul = []
    hx = hex(index / 0x5E * 0x100 + index % 0x5E + 0xB0A1)
    for i in range(2, len(hx) - 1, 2):
        hangul.append(r'\x' + hx[i:i+2])
    hangul = ''.join(hangul).decode('string-escape').decode('euc-kr')

    return hangul
