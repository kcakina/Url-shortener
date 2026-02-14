import pytest
from app.db import DB, TINY_URL


class TestSetLongAndShort:
    def test_returns_url_id(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        result = db.set_long_and_short(url)
        assert result == 1

    def test_stores_in_urls_objects(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        assert db.urls_objects[1] is url

    def test_stores_short_url_mapping(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        assert db.short_urls[url.shortUrl] == 1

    def test_stores_long_url_mapping(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        assert db.long_urls["https://example.com"] == 1

    def test_multiple_urls(self):
        db = DB()
        url1 = TINY_URL("https://example.com", 1)
        url2 = TINY_URL("https://google.com", 2)
        db.set_long_and_short(url1)
        db.set_long_and_short(url2)
        assert len(db.urls_objects) == 2
        assert len(db.short_urls) == 2
        assert len(db.long_urls) == 2


class TestGetObjectByShort:
    def test_returns_id_for_existing_short(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        result = db.get_object_by_short(url.shortUrl)
        assert result == 1

    def test_raises_for_missing_short(self):
        db = DB()
        with pytest.raises(ValueError, match="not found"):
            db.get_object_by_short("nonexistent")


class TestGetObjectByLong:
    def test_returns_id_for_existing_long(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        result = db.get_object_by_long("https://example.com")
        assert result == 1

    def test_raises_for_missing_long(self):
        db = DB()
        with pytest.raises(ValueError, match="not found"):
            db.get_object_by_long("https://notfound.com")


class TestGetObjectById:
    def test_returns_object_for_existing_id(self):
        db = DB()
        url = TINY_URL("https://example.com", 1)
        db.set_long_and_short(url)
        result = db.get_object_by_id(1)
        assert result is url

    def test_raises_for_missing_id(self):
        db = DB()
        with pytest.raises(ValueError, match="not found"):
            db.get_object_by_id(999)