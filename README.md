# hello-world

This is a tiny Flask application that exposes two endpoints:

- `POST /api/v1/hello/json` — accepts JSON payload and returns the same fields as JSON.
- `POST /api/v1/hello/xml` — accepts JSON payload and returns an XML response with `<xmlroot>` containing `<message>` and `<name>`.

Example request payload for both endpoints:

```
{
		"message": "Hello to all worlds!",
		````markdown
		# hello-world

		This is a tiny Flask application that exposes two endpoints:

		- `POST /api/v1/hello/json` — accepts JSON payload and returns the same fields as JSON.
		- `POST /api/v1/hello/xml` — accepts JSON payload and returns an XML response with `<xmlroot>` containing `<message>` and `<name>`.

		Example request payload for both endpoints:

		```
		{
				"message": "Hello to all worlds!",
				"name": "Ishaan G"
		}
		```

		Quick start (macOS, zsh):

		```bash
		cd python-projects/hello-world
		python3 -m venv .venv
		source .venv/bin/activate
		pip install -r requirements.txt
		# Run tests
		pytest -q
		# Run server
		python3 app.py
		```

		Requests example using `curl`:

		JSON endpoint:

		```bash
		curl -s -X POST http://localhost:5000/api/v1/hello/json \
		    -H "Content-Type: application/json" \
		    -d '{"message":"Hello to all worlds!","name":"Ishaan G"}'
		```

		XML endpoint:

		```bash
		curl -s -X POST http://localhost:5000/api/v1/hello/xml \
		    -H "Content-Type: application/json" \
		    -d '{"message":"Hello to all worlds!","name":"Ishaan G"}'
		```


		````

		Docker
		------

		Build and run with Docker (defaults to port 8081 inside container):

		```bash
		# build image
		docker build -t hello-world-app .

		# run container (container listens on $PORT inside the container; default 8081)
		docker run -e PORT=8081 -p 8081:8081 hello-world-app
		```

		Using docker-compose
		---------------------

		Start with default compose file (maps 8081:8081):

		```bash
		docker-compose up --build
		```

		To use the override file (example maps 8082:8082):

		```bash
		docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build
		```

		Notes:
		- The app reads the `PORT` environment variable (set in the Dockerfile/compose) and will listen on that port inside the container.
		- The `docker-compose.override.yml` in this repo is an example that sets `PORT=8082` and maps host port `8082` to container `8082`.

