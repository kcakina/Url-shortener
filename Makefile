venv:
	python3 -m venv .venv

activate:
	source .venv/bin/activate

install:
	.venv/bin/pip install -r requirements.txt

run:
	.venv/bin/python main.py

test-endpoint:
	curl http://localhost:8080/

test-create-url:
	curl -X POST http://localhost:8080/urls -H "Content-Type: application/json" -d '{"url": "https://example.com/some/long/path"}'

.PHONY: test
test:
	.venv/bin/pytest test/