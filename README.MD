## DockerBot

# Why?

Bootstrapping my Python programming learning with creating a functional bot that will become a test playground for many features. 

## Quick-Start

```
python main.py
```

## Main Menu

```
 ____   ___   ____ _  _______ ____  ____   ___ _____ 
|  _ \ / _ \ / ___| |/ / ____|  _ \| __ ) / _ \_   _|
| | | | | | | |   | ' /|  _| | |_) |  _ \| | | || |  
| |_| | |_| | |___| . \| |___|  _ <| |_) | |_| || |  
|____/ \___/ \____|_|\_\_____|_| \_\____/ \___/ |_|  
                                                     

Welcome to Dockerbot! A bot created in Python3 to help you automate some of those boring tasks

Please select an option:
1. Build Dockerfile
2. Exit Dockerbot

```

## Generating an LTS Dockerfile Example with NodeJs Using Dockerbot

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

## Generating a Specific Dockerfile Example Version Image with Ruby using Dockerbot

```
What programming language or framework do you want to use? (python, nodejs, java): ruby
What version to do you want to pull from Dockerhub? (lts, or specific docker tag): 2.7.3
What package manager do you want to install application dependencies with? (npm, yarn, pip): bundle
What operating system do you want to base your image on? (alpine, ubuntu): alpine
What packages or dependencies do you need? (comma-separated list): shared-mime-info
What ports do you need exposed to run this application? (comma-separated list): 3000
Here's your Dockerfile:
## Creating Base Image
FROM ruby:2.7.3-alpine

RUN apt-get install -y shared-mime-info

## Installing App Dependancies

RUN bundle install

## Adding App Files

COPY . /app

EXPOSE 3000

Enter a filename to save the Dockerfile: Dockerfile

Your Dockerfile has been saved to Dockerfile.

```
