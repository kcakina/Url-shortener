from app.db import DB, TINY_URL
from typing import Optional

def assign_short_url(db: DB, long_url: str, count: int) -> Optional[TINY_URL]:
    try:
        new_url = TINY_URL(long_url, url_id=count)
        db.set_long_and_short(new_url)
        return new_url
    except ValueError:
        return None