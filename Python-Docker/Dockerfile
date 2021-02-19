# Use alpine image as base image
FROM python:3.8.7-alpine

RUN pip install --upgrade pip
RUN pip install pipenv

# add tini and use 'ENTRYPOINT' to start and wrap CMD
# used to shut down app when you don't have access to source code 
ENTRYPOINT [ "/sbin/tini", "--"]

# Create a non-root user in Docker image
RUN adduser -D python

# Create the work dir and set permissions as WORKDIR set the permissions as root
RUN mkdir /home/python/app/ && chown -R python:python /home/python/app
# Sets the directory and creates the folder 
WORKDIR /home/python/app

# 'USER' sets the username (UID) when running the image
USER python

# After Dockerfile selects user, install dependencies of app
RUN pip install --user pipenv

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=python:python Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install --user -r requirements.txt

COPY --chown=python:python . .

# Execute the container
CMD ["python", "-u", "main.py"]

# validate that a container is still working
# HEALTHCHECK --interval=21s --timeout=3 --start-period=10s 
# CMD curl --fail http://localhost:3000/ || exit 1