import string

ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase
BASE = len(ALPHABET)
ID_OFFSET = 100_000_000


def encode_base62(num: int) -> str:
    if num == 0:
        return ALPHABET[0]

    chars = []
    while num > 0:
        num, rem = divmod(num, BASE)
        chars.append(ALPHABET[rem])

    return "".join(reversed(chars))


class TINY_URL:
    def __init__(self, long_url: str, url_id: int):
        self.id = url_id
        self.long_url = long_url
        self.hits = 0
        self.shortUrl = self.generate_short_urls()

    def generate_short_urls(self) -> str:
        return encode_base62(self.id + ID_OFFSET)


class DB:
    def __init__(self):
        self.long_urls = {}
        self.short_urls = {}

