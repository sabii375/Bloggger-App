# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Create a working directory in the container
WORKDIR /app

# Copy your Django project code into the container
COPY . /app/

# Install Django and other dependencies
RUN pip install -r requirements.txt

# Expose the port your Django app will run on
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
