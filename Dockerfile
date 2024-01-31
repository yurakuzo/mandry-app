# Base Stage
FROM python:3.11 as base

# Setup environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /usr/src/

# Install dependencies
RUN apt-get update && \
    apt-get install -y python3-dev python3-ldap python3-gevent python3-setuptools musl-dev gcc redis redis-server && \
    apt install netcat-traditional

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Copy and grant execution permissions to the start script
COPY entrypoint.sh /usr/src/
RUN chmod +x /usr/src/entrypoint.sh

# CMD ["/usr/src/entrypoint.sh"]