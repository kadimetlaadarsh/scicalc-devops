FROM python:3.11-slim

# Set working directory to project root inside container
WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py as a module
CMD ["python", "-m", "app.main"]
