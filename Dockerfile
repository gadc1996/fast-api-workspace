# Use the official Python image from the Docker Hub
FROM python:3.11-slim-bullseye

# Set the working directory in the container
WORKDIR /code

# Copy the dependencies file to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy rest of the app code
COPY ./app /code/app

# Expose the port the app runs on
EXPOSE 8080

# Serve the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]