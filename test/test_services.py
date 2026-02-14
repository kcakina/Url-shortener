from app.db import DB
from app.services import assign_short_url


class TestAssignShortUrl:
    def test_returns_tiny_url_object(self):
        db = DB()
        result = assign_short_url(db, "https://example.com", 1)
        assert result is not None
        assert result.long_url == "https://example.com"

    def test_sets_correct_id(self):
        db = DB()
        result = assign_short_url(db, "https://example.com", 5)
        assert result.id == 5

    def test_generates_short_url(self):
        db = DB()
        result = assign_short_url(db, "https://example.com", 1)
        assert result.shortUrl is not None
        assert len(result.shortUrl) > 0

    def test_stores_in_db(self):
        db = DB()
        result = assign_short_url(db, "https://example.com", 1)
        assert db.get_object_by_id(1) is result
        assert db.get_object_by_short(result.shortUrl) == 1
        assert db.get_object_by_long("https://example.com") == 1

    def test_multiple_urls_stored(self):
        db = DB()
        url1 = assign_short_url(db, "https://example.com", 1)
        url2 = assign_short_url(db, "https://google.com", 2)
        assert url1.shortUrl != url2.shortUrl
        assert len(db.urls_objects) == 2

    def test_hits_initialized_to_zero(self):
        db = DB()
        result = assign_short_url(db, "https://example.com", 1)
        assert result.hits == 0