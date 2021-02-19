# specify base image - use 'FROM' keyword
FROM python:3

# write the commands of copying the files and installing the dependencies
# set a working directory for the app
WORKDIR /usr/src/app

# copy all the files to the container for our app
COPY . .

# we have all the files so let's 
# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# specify the port number that needs to be exposed where flask app is running
# tell the port number the container should expose
EXPOSE 5000

# command to run application - use 'CMD' command
CMD ["python", "./app.py"]

