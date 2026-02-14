## URL Shortener Service

Build a simple REST service that shortens URLs and allows them to be resolved later.

The service should:
- accept a long URL
- generate a short identifier
- return the original URL when requested
- track how many times a short URL is used

Data can be stored in memory. Focus on clear API design and working behavior.

---

## REST Endpoints

### POST /urls
Create a shortened URL.

Request:
{
  "url": "https://example.com/some/long/path"
}

Response:
{
  "id": "abc123",
  "shortUrl": "/u/abc123"
}

---

### GET /u/{id}
Resolve a short URL.

Response:
{
  "url": "https://example.com/some/long/path"
}

Behavior:
- Increment hit counter each time this endpoint is called.
- Return 404 if the id does not exist.

---

### GET /urls/{id}
Get metadata for a shortened URL.

Response:
{
  "id": "abc123",
  "url": "https://example.com/some/long/path",
  "hits": 5
}

---

## Rules

- IDs must be unique.
- Store data in memory.
- Return appropriate errors for invalid or missing resources.
