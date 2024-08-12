# Use the official Python image with Spark
FROM bitnami/spark:3.5.0

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY src/ ./src/
COPY tests/ ./tests/

# Set environment variables
ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH="$PATH:/.local/bin"
# Command to run tests
CMD ["python3", "-m","pytest", "tests/"]
