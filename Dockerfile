# Base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the project files into the container
COPY . /app/

WORKDIR /app/weatherapp
# Expose port 8000 (Django's default port)
EXPOSE 8000

# Command to run the Django development server
CMD ["sh", "-c", "python manage.py test && python manage.py runserver 0.0.0.0:8000"]