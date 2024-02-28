# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies required for building Python packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
    # If you encounter other similar compilation issues, you might need additional packages like 'libffi-dev' or 'libssl-dev'.
    && rm -rf /var/lib/apt/lists/*

# Download dependencies with caching to speed up builds.
# Note: Make sure you have 'requirements.txt' available at build context.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt,readonly \
    python -m pip install -r requirements.txt

# Switch to the non-privileged user.

# Copy the source code.
COPY . .

RUN python3 manage.py collectstatic --no-input

# Expose the application port.
EXPOSE 8000

# Run the application.
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
