from enc.b64 import b64d, b64e, byts, sprint, unprint


def test_b64():
    out = b64e(byts('Hello World!!'))
    print(sprint(out))
    print(unprint(sprint(out)))
    print(b64d(unprint(sprint(out))))
    print(b64d(out))
    s1c1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    c1e = b64e(bytearray.fromhex(s1c1))
    print(sprint(c1e))
    print(b64d(c1e))


test_b64()
