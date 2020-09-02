def reverseByte(byte, cache={}):
    if byte not in cache:
        cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023
    return cache[byte]

def reverseI32(n):
    ret, power = 0, 24
    cache = dict()
    while n:
        ret += reverseByte(n & 0xff, cache) << power
        n = n >> 8
        power -= 8
    return ret


def reverseI32(n):
    n = (n >> 16) | (n << 16)  # 16位交换
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) # 每八位交换
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    return n

print(reverseI32(0b01))


