class SHA1:
    def __init__(self, message):
        self._h0 = 0x67452301
        self._h1 = 0xEFCDAB89
        self._h2 = 0x98BADCFE
        self._h3 = 0x10325476
        self._h4 = 0xC3D2E1F0
        self.message_in_bytes = str()
        self.message = message

    def _prepare_data(self):
        for n in range(len(self.message)):
            self.message_in_bytes += '{0:08b}'.format(ord(self.message[n]))

        bits = self.message_in_bytes + "1"
        padding = bits

        while len(padding) % 512 != 448:
            padding += "0"

        padding += '{0:064b}'.format(len(bits) - 1)

        return padding

    def _chunk_data(self, l, n):
        return [l[i:i + n] for i in range(0, len(l), n)]

    def _shift(self, n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    def _main_loop(self):
        padding = self._prepare_data()
        for c in self._chunk_data(padding, 512):
            words = self._chunk_data(c, 32)
            w = [0] * 80

            for n in range(0, 16):
                w[n] = int(words[n], 2)
            for i in range(16, 80):
                w[i] = self._shift((w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]), 1)

            a = self._h0
            b = self._h1
            c = self._h2
            d = self._h3
            e = self._h4

            for i in range(0, 80):
                if 0 <= i <= 19:
                    f = (b & c) | ((~b) & d)
                    k = 0x5A827999
                elif 20 <= i <= 39:
                    f = b ^ c ^ d
                    k = 0x6ED9EBA1
                elif 40 <= i <= 59:
                    f = (b & c) | (b & d) | (c & d)
                    k = 0x8F1BBCDC
                elif 60 <= i <= 79:
                    f = b ^ c ^ d
                    k = 0xCA62C1D6

                temp = self._shift(a, 5) + f + e + k + w[i] & 0xffffffff
                e = d
                d = c
                c = self._shift(b, 30)
                b = a
                a = temp

            self._h0 = self._h0 + a & 0xffffffff
            self._h1 = self._h1 + b & 0xffffffff
            self._h2 = self._h2 + c & 0xffffffff
            self._h3 = self._h3 + d & 0xffffffff
            self._h4 = self._h4 + e & 0xffffffff

        return '%08x%08x%08x%08x%08x' % (self._h0, self._h1, self._h2, self._h3, self._h4)

    def hash_message(self):
        return self._main_loop()


sha1 = SHA1("hello world")
print(sha1.hash_message())
