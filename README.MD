## DockerBot

# Why?

Bootstrapping my Python programming learning with creating a functional bot that will become a test playground for many features.


## Quick-Start


```
python3 main.py
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
2. Generate Docker Compose
3. Inspect Dockerfile
4. Chat with Dockerbot
5. Exit Dockerbot
```


## Using Dockerbot like ChatGPT

If you don't want to be walked through a Dockerfile install, you can select option 4 to be able to pass a prompt into Dockerbot like ChatGPT.

Requirements: 

You will need to add in your `openai api key` in `main.py` order for this to work.
```
 ____   ___   ____ _  _______ ____  ____   ___ _____ 
|  _ \ / _ \ / ___| |/ / ____|  _ \| __ ) / _ \_   _|
| | | | | | | |   | ' /|  _| | |_) |  _ \| | | || |  
| |_| | |_| | |___| . \| |___|  _ <| |_) | |_| || |  
|____/ \___/ \____|_|\_\_____|_| \_\____/ \___/ |_|  
                                                     

Enter a prompt to generate a Dockerfile: Generate me a Nodejs latest dockerfile
Here's your Dockerfile:


FROM node:latest

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "index.js" ]

Enter a filename to save the Dockerfile: Dockerfile

Your Dockerfile has been saved to Dockerfile.


Please select an option:
1. Build Dockerfile
2. Generate Docker Compose
3. Inspect Dockerfile
4. Chat with Dockerbot
5. Exit Dockerbot
```

## Adding To The Bot Knowledge base

```
 ____   ___   ____ _  _______ ____  ____   ___ _____ 
|  _ \ / _ \ / ___| |/ / ____|  _ \| __ ) / _ \_   _|
| | | | | | | |   | ' /|  _| | |_) |  _ \| | | || |  
| |_| | |_| | |___| . \| |___|  _ <| |_) | |_| || |  
|____/ \___/ \____|_|\_\_____|_| \_\____/ \___/ |_|  
                                                     

What programming language or framework do you want to use? (python, nodejs, java): my-newest-image
Sorry, {language} is not supported. Would you like to add it to our knowledge base? (y/n): y
Enter the image name: my-newest-image
Enter the image tag(lts or a specific version): lts
my-newest-image image added to the knowledge base with image name my-newest-image

```

Which creates a new entry in your `docker_images.py` file

```
  
  "my-newest-image": ['FROM my-newest-image:lts'],

```

## Generate App Dependencies Manually or Automatically

```
Do you want to input dependencies manually or read from a file such as package.json? (m/f): f
Enter the name of the file containing dependencies (e.g. package.json): package.json
What ports do you need exposed to run this application? (comma-separated list): 5000

Here's your Dockerfile:

## Creating Base Image

FROM nodejs:lts-alpine

RUN npm install

COPY package.json /app/package.json

## Adding App Files

COPY . /app

EXPOSE 5000

Enter a filename to save the Dockerfile: Dockerfile

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

## Generating docker-compose.yaml files based on Dockerfile

```
 ____   ___   ____ _  _______ ____  ____   ___ _____
|  _ \ / _ \ / ___| |/ / ____|  _ \| __ ) / _ \_   _|
| | | | | | | |   | ' /|  _| | |_) |  _ \| | | || |
| |_| | |_| | |___| . \| |___|  _ <| |_) | |_| || |
|____/ \___/ \____|_|\_\_____|_| \_\____/ \___/ |_|

Enter the path to the Dockerfile: ./Dockerfile

Here's your docker-compose.yaml:

version: '3'

services:
  nodejs:
    build:
      context: .


Enter a filename to save the docker-compose.yaml: docker-compose.yaml

Your docker-compose.yaml has been saved to docker-compose.yaml.

```

## Inspecting A Dockerfile and its directory contents

```
 ____   ___   ____ _  _______ ____  ____   ___ _____ 
|  _ \ / _ \ / ___| |/ / ____|  _ \| __ ) / _ \_   _|
| | | | | | | |   | ' /|  _| | |_) |  _ \| | | || |  
| |_| | |_| | |___| . \| |___|  _ <| |_) | |_| || |  
|____/ \___/ \____|_|\_\_____|_| \_\____/ \___/ |_|  
                                                     

Welcome to Dockerbot! A bot created in Python3 to help you automate some of those boring tasks

Please select an option:
1. Build Dockerfile
2. Generate Docker Compose
3. Inspect Dockerfile
4. Exit Dockerbot
> 3

Enter the path to the Dockerfile: Dockerfile

Here's the description of your Dockerfile:

This Dockerfile uses python:3.9-slim-buster as the base image 

Installs the following packages: pyfiglet, openai, flask. 

It also exposes the following ports: 80, 6001, 5000.

Please select an option:
1. Build Dockerfile
2. Generate Docker Compose
3. Inspect Dockerfile
4. Exit Dockerbot
```
