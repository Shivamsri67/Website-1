FROM python:3.11

WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install boto3
# Copy the rest of the application files
COPY . .

# Expose port 8000 for Django
EXPOSE 8000

# Default command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
