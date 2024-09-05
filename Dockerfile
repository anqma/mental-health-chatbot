# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy necessary files into the container
COPY data/Mental_Health_FAQ.csv data/Mental_Health_FAQ.csv
COPY requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY mental_health_assistant .

#Expose port 5000
EXPOSE 5000

# Set the default command to run Streamlit
CMD ["streamlit", "run", "app.py"]