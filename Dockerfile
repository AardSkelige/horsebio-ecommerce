FROM python:alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Set the working directory in the container
WORKDIR /code

ADD . /code/
ADD .env.docker /code/.env

# Copy the dependencies file to the container
COPY requirements.txt /code/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code to the container
COPY . /code/
