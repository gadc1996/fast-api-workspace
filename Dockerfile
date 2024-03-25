# Python image to use.
FROM python:3.11-slim-bullseye

# Set the working directory to /app
WORKDIR /app


# Install apt-get packages
RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    default-libmysqlclient-dev \
    gcc

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install gunicorn

# Copy the rest of the working directory contents into the container at /app
COPY src/. .

# Expose port 8080
EXPOSE 8080

# Run migrations and start server
ENTRYPOINT python manage.py migrate && gunicorn --bind 0.0.0.0:8080 core.wsgi:application
