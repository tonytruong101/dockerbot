import random
import sys

# Define a knowledge base of Dockerfile commands based on user inputs
knowledge_base = {
    "python": ["FROM python:3.9", "RUN pip install -r requirements.txt"],
    "nodejs": ["RUN npm install"],
    "java": ["FROM openjdk:11", "COPY target/*.jar /app.jar"],
    "ruby": ["FROM ruby"]
}

# Define a chatbot interface to prompt the user for input
def prompt_user():
    print("Welcome to Dockerbot! Let's create a Dockerfile.")
    language       = input("What programming language or framework do you want to use? (python, nodejs, java): ")
    version        = input("What version to do you want to pull from Dockerhub? (lts, or specific docker tag ")
    packageManager = input("What package manager do you wan to install application dependancies with? (npm, yarn, pip):")
    os             = input("What operating system do you want to base your image on? (alpine, ubuntu): ")
    dependencies   = input("What packages or dependencies do you need? (comma-separated list): ")
    ports          = input("What ports do you need exposed to run this application? (comma-seperated lst):")
    return (language, version, packageManager, os, dependencies, ports)

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

# Main program loop
while True:
    user_input = prompt_user()
    language, version, packageManager, os, dependencies, ports = user_input
    dockerfile = generate_dockerfile(language, version, packageManager, os, dependencies, ports)
    print(f"Here's your Dockerfile:\n{dockerfile}\n")
    filename = input("Enter a filename to save the Dockerfile: ")
    write_dockerfile(filename, dockerfile)
    print(f"Your Dockerfile has been saved to {filename}.\n")
    response = input("Do you want to create another Dockerfile? (y/n): ")
    if response.lower() == "n":
        close_app()

