## DockerBot

A project created to learn Python Programming. A functional Docker bot that will generate Dockerfiles for most basic web applications. This may grow to become bigger overtime as I find more time to invest into the project.

## Quick-Start

```
python main.py
```

## Generating a Dockerfile Example with NodeJs Using Dockerbot

```
Welcome to Dockerbot! Let's create a Dockerfile.
What programming language or framework do you want to use? (python, nodejs, java): nodejs
What version to do you want to pull from Dockerhub? (lts, or specific docker tag lts
What package manager do you wan to install application dependancies with? (npm, yarn, pip):npm
What operating system do you want to base your image on? (alpine, ubuntu): alpine
What packages or dependencies do you need? (comma-separated list): vim, git, postgresql, shared-mime-info
What ports do you need exposed to run this application? (comma-seperated lst):80,8080,3000

Here is your Dockerfile:

---------------------
## Creating Base Image
FROM nodejs:lts-alpine

RUN apt-get install -y vim
RUN apt-get install -y  git
RUN apt-get install -y  postgresql
RUN apt-get install -y  shared-mime-info

## Installing App Dependancies

RUN npm install

## Adding App Files

COPY . /app

EXPOSE 80

EXPOSE 8080

EXPOSE 3000
---------------------

Enter a filename to save the Dockerfile: Dockerfile

Your Dockerfile has been saved to Dockerfile.

Do you want to create another Dockerfile? (y/n): n

Goodbye! 

```

