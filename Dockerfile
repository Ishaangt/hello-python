FROM python:3.11-slim

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy source
COPY . /app

# Default port (can be overridden by docker-compose or docker run -e PORT=...)
ENV PORT=8081
EXPOSE 8081

# Start the app (app reads PORT env or -p flag)
CMD ["python", "app.py"]
