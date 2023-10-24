def caeser(byt: bytes, amt: int, start: int = ord('A'), end: int = ord('Z')) -> bytes:
    enc = b''
    for b in byt:
        if b < start or b > end:
            enc += b.to_bytes(1, byteorder='little')
        else:
            enc += (start + (b - start + amt) % (end + 1 - start)).to_bytes(1, byteorder='little')
    return enc


def test_caeser():
    assert caeser(b'HELLO', 26) == b'HELLO'
    assert caeser(b'ATTACK AT DAWN', 1) == b'BUUBDL BU EBXO'
    assert caeser(b'THIS IS NOT LATIN', 13) == b'GUVF VF ABG YNGVA'
    assert caeser(b'this is not latin', 16) == b'this is not latin'
    assert caeser(b'this is not latin', 13, start=ord('a'), end=ord('z')) == b'guvf vf abg yngva'


if __name__ == "__main__":
    test_caeser()
