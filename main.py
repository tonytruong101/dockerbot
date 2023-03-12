import random
import sys

# Define a knowledge base of Dockerfile commands based on user inputs

knowledge_base = {
    "python":                ["FROM python:3.9", "RUN pip install -r requirements.txt"],
    "nodejs":                  ["FROM node:latest", "RUN npm install"],
    "mysql":                 ["FROM mysql:latest", "ENV MYSQL_ROOT_PASSWORD=password", "COPY init.sql /docker-entrypoint-initdb.d/"],
    "postgres":              ["FROM postgres:latest", "ENV POSTGRES_PASSWORD=password", "COPY init.sql /docker-entrypoint-initdb.d/"],
    "mongo":                 ["FROM mongo:latest", "COPY init.js /docker-entrypoint-initdb.d/", "CMD mongod --bind_ip_all"],
    "redis":                 ["FROM redis:latest"],
    "nginx":                 ["FROM nginx:latest", "COPY nginx.conf /etc/nginx/nginx.conf"],
    "php":                   ["FROM php:latest", "COPY index.php /var/www/html/"],
    "alpine":                ["FROM alpine:latest"],
    "golang":                ["FROM golang:latest", "COPY main.go .", "RUN go build -o main"],
    "microsoft/dotnet":      ["FROM mcr.microsoft.com/dotnet/sdk:latest", "COPY . /app", "WORKDIR /app", "RUN dotnet restore", "RUN dotnet build"],
    "centos":                ["FROM centos:latest"],
    "debian":                ["FROM debian:latest"],
    "amazonlinux":           ["FROM amazonlinux:latest"],
    "ubuntu":                ["FROM ubuntu:latest"],
    "httpd":                 ["FROM httpd:latest", "COPY index.html /usr/local/apache2/htdocs/"],
    "grafana/grafana":       ["FROM grafana/grafana:latest"],
    "jenkins":               ["FROM jenkins/jenkins:latest"],
    "bitnami/kafka":         ["FROM bitnami/kafka:latest"],
    "prom/prometheus":       ["FROM prom/prometheus:latest"],
    "alpine/git":            ["FROM alpine/git:latest"],
    "elastic/elasticsearch": ["FROM docker.elastic.co/elasticsearch/elasticsearch:latest"],
    "amazon/dynamodb-local": ["FROM amazon/dynamodb-local:latest"],
    "consul":                ["FROM consul:latest"],
    "ruby":                  [{"FROM ruby"}]
}

def prompt_user():
    language = input("What programming language or framework do you want to use? (python, nodejs, java): ")
    version = input("What version to do you want to pull from Dockerhub? (lts, or specific docker tag): ")
    packageManager = input("What package manager do you want to install application dependencies with? (npm, yarn, pip): ")
    os = input("What operating system do you want to base your image on? (alpine, ubuntu): ")
    dependencies = input("What packages or dependencies do you need? (comma-separated list): ")
    ports = input("What ports do you need exposed to run this application? (comma-separated list): ")

    return language, version, packageManager, os, dependencies, ports


def main_menu():
    print("Welcome to Dockerbot! A bot created in Python3 to help you automate some of those boring tasks")
    
    while True:
        print("\nPlease select an option:")
        print("1. Build Dockerfile")
        print("2. Exit Dockerbot")

        choice = input("> ")

        if choice == "1":
            response = "y"
            while response.lower() =="y":
              user_input = prompt_user()
              language, version, packageManager, os, dependencies, ports = user_input
              dockerfile = generate_dockerfile(language, version, packageManager, os, dependencies, ports)
              print(f"Here's your Dockerfile:\n{dockerfile}\n")
              filename = input("Enter a filename to save the Dockerfile: ")
              write_dockerfile(filename, dockerfile)
              print(f"Your Dockerfile has been saved to {filename}.\n")
              response = input("Do you want to create another Dockerfile? (y/n): ")
        elif choice == "2":
            print("Thank you for using Dockerbot. Goodbye!")
            sys.exit()  # Exit the entire program
        else:
            print("Invalid choice. Please try again.")

#def prompt_user():
#    language       = input("What programming language or framework do you want to use? (python, nodejs, java): ")
#    version        = input("What version to do you want to pull from Dockerhub? (lts, or specific docker tag ")
#    packageManager = input("What package manager do you wan to install application dependancies with? (npm, yarn, pip):")
#    os             = input("What operating system do you want to base your image on? (alpine, ubuntu): ")
#    dependencies   = input("What packages or dependencies do you need? (comma-separated list): ")
#    ports          = input("What ports do you need exposed to run this application? (comma-seperated lst):")
    
#    return language, version, packageManager, os, dependencies, ports

# Generate the Dockerfile based on user inputs

def generate_dockerfile(language, version, packageManager, os, dependencies, ports):
    base_commands = knowledge_base.get(language, [])
    if os == "alpine":
        image_tag = f"FROM {language}:{version}-{os}"
    else:
        image_tag = f"FROM {language}:{version}"
    base_commands[0] = f"## Creating Base Image\n{image_tag}\n"

    install_commands = []
    if dependencies:
        dependencies = dependencies.split(",")
        for dep in dependencies:
            install_commands.append(f"RUN apt-get install -y {dep}")
        install_commands.append("\n## Installing App Dependancies")
        install_commands.append(f"\nRUN {packageManager} install")
    all_commands = base_commands + install_commands

    app_commands = []
    app_commands.append("\n## Adding App Files")
    app_commands.append("\nCOPY . /app")     
    if ports:
        ports = ports.split(",")
        for port in ports:
            app_commands.append(f"\nEXPOSE {port}")

    all_commands += app_commands

    return "\n".join(all_commands)

# Write the Dockerfile to a file
def write_dockerfile(filename, dockerfile):
    with open(filename, "w") as f:
        f.write(dockerfile)

# Close the app
def close_app():
    print("Goodbye!")
    sys.exit()

# Mainmenu program loop

while True:     
    main_menu()
