from app.db import TINY_URL, encode_base62, ID_OFFSET


class TestEncodeBase62:
    def test_zero(self):
        assert encode_base62(0) == "0"

    def test_single_digit(self):
        assert encode_base62(9) == "9"

    def test_lowercase_range(self):
        assert encode_base62(10) == "a"

    def test_uppercase_range(self):
        assert encode_base62(36) == "A"

    def test_large_number(self):
        result = encode_base62(99999)
        assert isinstance(result, str)
        assert len(result) > 0



class TestTinyURL:
    def test_init_sets_long_url(self):
        url = TINY_URL("https://example.com", 1)
        assert url.long_url == "https://example.com"

    def test_init_sets_id(self):
        url = TINY_URL("https://example.com", 42)
        assert url.id == 42

    def test_init_hits_zero(self):
        url = TINY_URL("https://example.com", 1)
        assert url.hits == 0

    def test_short_url_generated(self):
        url = TINY_URL("https://example.com", 1)
        assert url.shortUrl == encode_base62(1 + ID_OFFSET)

    def test_different_ids_produce_different_short_urls(self):
        url1 = TINY_URL("https://example.com", 1)
        url2 = TINY_URL("https://example.com", 2)
        assert url1.shortUrl != url2.shortUrl

    def test_short_url_for_zero_id(self):
        url = TINY_URL("https://example.com", 0)
        assert url.shortUrl == encode_base62(ID_OFFSET)
        assert len(url.shortUrl) >= 5

    def test_short_url_for_large_id(self):
        url = TINY_URL("https://example.com", 100000)
        assert url.shortUrl == encode_base62(100000 + ID_OFFSET)