# PULL BASE IMAGE
FROM python:3.9.6-slim-buster

# SET WORKING DIRECTORY
WORKDIR /chat-webapp

# SET ENVIRONMENT VARIABLES
ENV PYTHONDONOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERD 1

# INSTALL SYSTEM DEPENDENCIES
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# INSTALL PYTHON DEPENDENCIES
COPY ./requirements.txt /chat-webapp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /chat-webapp/requirements.txt

# ADD APP
COPY . .