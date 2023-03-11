# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
RUN apt-get update && apt-get install -y vim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]
