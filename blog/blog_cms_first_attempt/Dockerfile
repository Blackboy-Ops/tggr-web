FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    build-essential libpq-dev gettext \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run app with gunicorn
CMD ["gunicorn", "blog_cms.wsgi:application", "--bind", "0.0.0.0:8000"]
