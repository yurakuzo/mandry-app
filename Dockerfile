FROM python:3.11-alpine

# Setup environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_ROOT_USER_ACTION=ignore

WORKDIR /usr/src/

# Install dependencies
RUN apk update && apk add --no-cache postgresql-dev python3-dev musl-dev gcc

# Install Python dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 5000

# Copy and grant execution permissions to the start script
COPY ./entrypoint.sh /usr/src/
RUN chmod +x /usr/src/entrypoint.sh

ENTRYPOINT [ "/usr/src/entrypoint.sh" ]