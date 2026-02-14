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
        self.urls_objects = {} # id > objects
        self.short_urls = {} # short to id
        self.long_urls = {} # long to id

    def set_long_and_short(self, url: TINY_URL)-> int:
        self.urls_objects[url.id] = url
        self.short_urls[url.shortUrl] = url.id
        self.long_urls[url.long_url] = url.id

        return url.id

    def get_object_by_short(self, short: str) -> TINY_URL:
        if short in self.short_urls:
            return self.short_urls[short]
        raise ValueError(f'url: {short} not found')

    def get_object_by_long(self, long: str) ->TINY_URL:
        if long in self.long_urls:
            return self.long_urls[long]
        raise ValueError(f'url: {long} not found')

    def get_object_by_id(self, url_id: int)-> TINY_URL:
        if url_id in self.urls_objects:
            return self.urls_objects[url_id]
        raise ValueError(f'url_id: {url_id} not found')

