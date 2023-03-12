from docker_images import knowledge_base
from generate_docker_compose import generate_docker_compose
import random
import sys
import pyfiglet
import json

# Set the text to be displayed
text = "DOCKERBOT"

# Use the Pyfiglet library to generate ASCII art
ascii_art = pyfiglet.figlet_format(text)

def prompt_user():
    print(ascii_art)
    language = input("What programming language or framework do you want to use? (python, nodejs, java): ")
    version = input("What version to do you want to pull from Dockerhub? (lts, or specific docker tag): ")
    packageManager = input("What package manager do you want to install application dependencies with? (npm, yarn, pip): ")
    os = input("What operating system do you want to base your image on? (alpine, ubuntu): ")
    dependencies_choice = input("Do you want to input dependencies manually or read from a file such as package.json? (m/f): ")
    dependencies = []
    if dependencies_choice.lower() == "m":
        dependencies = input("What packages or dependencies do you need? (comma-separated list): ")
    elif dependencies_choice.lower() == "f":
        filename = input("Enter the name of the file containing dependencies (e.g. package.json): ")
        with open(filename, "r") as f:
            dependencies_data = json.load(f)
        if "dependencies" in dependencies_data:
            dependencies = ",".join(dependencies_data["dependencies"])
        else:
            print(f"No dependencies found for {language}. Please provide the dependencies manually.")
            dependencies = input("What packages or dependencies do you need? (comma-separated list): ")

    ports = input("What ports do you need exposed to run this application? (comma-separated list): ")

    return language, version, packageManager, os, dependencies, ports


def main_menu():
    print(ascii_art)
    print("Welcome to Dockerbot! A bot created in Python3 to help you automate some of those boring tasks")
    
    while True:
        print("\nPlease select an option:")
        print("1. Build Dockerfile")
        print("2. Generate Docker Compose")
        print("3. Exit Dockerbot")

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
              print(f"\nYour Dockerfile has been saved to {filename}.\n")
              response = input("Do you want to create another Dockerfile? (y/n): ")
        elif choice == "2":
            print(ascii_art)
            dockerfile_path = input("Enter the path to the Dockerfile: ")
            composefile = generate_docker_compose(dockerfile_path)
            print(f"Here's your docker-compose.yaml:\n{composefile}\n")
            filename = input("Enter a filename to save the docker-compose.yaml: ")
            write_dockerfile(filename, composefile)
            print(f"\nYour docker-compose.yaml has been saved to {filename}.\n")
        elif choice == "3":
            print(ascii_art)
            print("Thank you for using Dockerbot. Goodbye!")
            sys.exit()  # Exit the entire program
        else:
            print("Invalid choice. Please try again.")

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
        if packageManager == "npm":
            for dep in dependencies:
                install_commands.append(f"RUN npm install {dep}")
        elif packageManager == "yarn":
            for dep in dependencies:
                install_commands.append(f"RUN yarn add {dep}")
        elif packageManager == "bundler":
            for dep in dependencies:
                install_commands.append(f"RUN gem bundle add {dep}")
        # Add other package manager options here...
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
