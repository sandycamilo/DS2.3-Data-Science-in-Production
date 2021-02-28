FROM python:3.7-slim-buster

# Add requirements.txt file 
COPY . .

# Install required pyhton dependencies from requirements file 
RUN pip install -r requirements.txt

ADD . /app

# Set working directory to previously added app directory
WORKDIR /app

# Expose the port Flask is running on 
EXPOSE 5000

# Command to run application
CMD ["python3", "./application.py"]
