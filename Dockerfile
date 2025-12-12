FROM python:3.11-slim

# Install necessary OS packages (curl used in HEALTHCHECK)
RUN apt-get update && apt-get install -y --no-install-recommends \
		curl \
 && rm -rf /var/lib/apt/lists/*

# Create a non-root user and home directory
RUN groupadd -r app && useradd -r -g app -m -d /home/app app

WORKDIR /home/app

# Copy requirements and create a virtualenv in the app user's home
COPY requirements.txt /home/app/requirements.txt
RUN python3 -m venv /home/app/.venv \
 && /home/app/.venv/bin/pip install --upgrade pip setuptools wheel

# Install requirements as the non-root user into the venv to avoid pip root warnings
RUN chown -R app:app /home/app
USER app
ENV PATH="/home/app/.venv/bin:$PATH"
RUN /home/app/.venv/bin/pip install --no-cache-dir -r /home/app/requirements.txt

# Copy application source as non-root user
COPY --chown=app:app . /home/app

# Default port (can be overridden by docker-compose or docker run -e PORT=...)
ENV PORT=8081
EXPOSE 8081

# Docker healthcheck (uses curl inside container)
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
	CMD curl -f http://127.0.0.1:${PORT}/health || exit 1

# Start the app (app reads PORT env or -p flag)
CMD ["python", "app.py"]
