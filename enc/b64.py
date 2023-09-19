def b64e(byts: bytearray) -> bytearray:
    """ change bytes to bytearray of b64 values
    """
    l = 4 * int(len(byts) / 3)
    if len(byts) % 3 != 0:
        l += (len(byts) % 3) + 1
    res = bytearray(l)
    i = 0
    for j in range(0, l, 4):
        b1 = byts[i]
        if i + 1 < len(byts):
            b2 = byts[i + 1]
        else:
            b2 = 0
        if i + 2 < len(byts):
            b3 = byts[i + 2]
        else:
            b3 = 0
        res[j] = (0xfc & b1) >> 2
        res[j + 1] = ((0x3 & b1) << 4) + ((0xf0 & b2) >> 4)
        if j + 2 == len(res):
            break
        res[j + 2] = ((0xf & b2) << 2) + ((0xc0 & b3) >> 6)
        if j + 3 == len(res):
            break
        res[j + 3] = 0x3f & b3
        i += 3
    return res


def b64d(byts: bytearray) -> bytearray:
    l = 3*int(len(byts)/4)
    if len(byts) % 4 == 1:
        raise ValueError("invalid base64")
    elif len(byts) % 4 == 2:
        l += 1
    elif len(byts) % 4 == 3:
        l += 2
    res = bytearray(l)
    i = 0
    for j in range(0, l, 3):
        b1 = byts[i]
        b2 = byts[i+1]
        if i + 2 < len(byts):
            b3 = byts[i+2]
        else:
            b3 = 0
        if i + 3 < len(byts):
            b4 = byts[i+3]
        else:
            b4 = 0

        res[j] = (b1 << 2) + ((0x30 & b2) >> 4)
        if j + 1 == len(res):
            break
        res[j+1] = ((0xf & b2) << 4) + ((0x3c & b3) >> 2)
        if j + 2 == len(res):
            break
        res[j+2] = ((0x3 & b3) << 6) + b4
        i += 4
    return res


def byts(a: str) -> bytearray:
    """ shortcut for creating a bytearray from an ascii string """
    return bytearray(a.encode(encoding='ascii'))


def sprint(byt: bytearray, filesafe=False) -> str:
    if not filesafe:
        b64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    else:
        b64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    s = ''
    for b in byt:
        s += b64_charset[b]
    return s


def unprint(s: str, filesafe=False) -> bytearray:
    """
    convert a base64 string to a bytearray of b64 values
    :param s: input string
    :param filesafe: use filesafe charset if true
    :return: bytesarray of b64 values

    can raise ValueError if s contains invalid b64 characters
    """
    if not filesafe:
        b64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    else:
        b64_charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
    res = bytearray(len(s))
    for i in range(len(res)):
        if s[i] == '=':
            break
        res[i] = b64_charset.index(s[i])
    return res

