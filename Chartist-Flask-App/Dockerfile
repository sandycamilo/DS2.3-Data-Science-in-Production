FROM python:3.7-slim-buster

# Add requirements.txt file 
COPY requirements.txt /requirements.txt 

# Install required pyhton dependencies from requirements file 
RUN pip install -r requirements.txt

ADD . /app

# Set working directory to previously added app directory
WORKDIR /app

# Expose the port Flask is running on 
EXPOSE 5000

# Command to run application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
