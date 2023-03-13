from docker_images import knowledge_base
from generate_docker_compose import generate_docker_compose
from dockerfile_analysis import analyze_dockerfile
from validations.version_validation import validate_version
from validations.package_manager_validation import validate_package_manager

import random
import sys
import pyfiglet
import json
import openai

openai.api_key = ''

# Set the text to be displayed
text = "DOCKERBOT"

# Use the Pyfiglet library to generate ASCII art
ascii_art = pyfiglet.figlet_format(text)

knowledge_base_file = "docker_images.py"

def file_exists(filename):
    try:
        with open(filename) as f:
            return True
    except FileNotFoundError:
        return False

def write_to_file(knowledge_base):
    with open(knowledge_base_file, "w") as f:
        f.write("knowledge_base = {\n")
        for k, v in knowledge_base.items():
            f.write(f'    "{k}": {v},\n')
        f.write("}\n")

def generate_dockerfile_from_prompt(prompt):
    while True:
        # Check if the user prompt contains the word "Docker" or "docker"
        if not any(word in prompt.lower() for word in ["docker", "Docker"]):
            print("Invalid prompt. Please enter a Docker related prompt.")
            prompt = input("Enter a Docker related prompt: ")
            continue


        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text


        # Filter out prompts that do not contain the word "Docker" or "docker"

        print(f"Here's your file:\n{message}\n")

        while True:
            response = input("Do you accept this response? (y/n): ")
            if response.lower() == "y":
                return message
            elif response.lower() == "n":
                prompt = input("Enter a Docker related prompt: ")
                break
            else:
                print("Invalid input. Please enter 'y' to accept or 'n' to regenerate.")

def prompt_user():
    print(ascii_art)

    global knowledge_base

    if file_exists(knowledge_base_file):
        # if knowledge base file exists, import its contents
        from docker_images import knowledge_base
    else:
        # otherwise, initialize an empty knowledge base
        knowledge_base = {}

    knowledge_base_list = list(knowledge_base.keys())

    language = ""    

    while True:
        language = input("What programming language or framework do you want to use? (python, nodejs, java): ")

        if language.lower() == 'exit' or language.lower() == 'quit':
            main_menu() 

        if language not in knowledge_base:
            add_custom = input("Sorry, {language} is not supported. Would you like to add it to our knowledge base? (y/n): ")
            if add_custom.lower() == "y":
                custom_image = input("Enter the image name: ")
                custom_image_tag = input("Enter the image tag(lts or a specific version): ")
                knowledge_base[language] = ['FROM {}:{}'.format(custom_image, custom_image_tag)]
                print(f"{language} image added to the knowledge base with image name {custom_image}")
                write_to_file(knowledge_base)  # write the updated knowledge base to file
            else:
                print(f"Please choose from: {knowledge_base_list}")
        else:
            print(f"{language} image: {knowledge_base[language]}")
            break

    version = input("What version to do you want to pull from Dockerhub? (lts, or specific docker tag): ")

    if version.lower() == 'exit' or version.lower() == 'quit':
        main_menu()

    version = validate_version(version)

    packageManager = input("What package manager do you want to install application dependencies with? (npm, yarn, pip): ")

    if packageManager.lower() == 'exit' or packageManager.lower() == 'quit':
        main_menu()

    packageManager = validate_package_manager(packageManager)

    os = input("What operating system do you want to base your image on? (alpine, ubuntu): ")

    if os.lower() == 'exit' or os.lower() == 'quit':
        main_menu()

    dependencies_choice = input("Do you want to input dependencies manually or read from a file such as package.json? (m/f): ")

    if dependencies_choice.lower() == 'exit' or dependencies_choice.lower() == 'quit':
        main_menu()

    while dependencies_choice not in ["m", "f"]: # Add valid options for dependencies choice
         dependencies_choice = input("Invalid input. Please enter a valid option from the list (m/f): ")

    dependencies = [] 

    if dependencies_choice.lower() == "m":
        dependencies = input("What packages or dependencies do you need? (comma-separated list): ")
    elif dependencies_choice.lower() == "f":
        pass

    ports = input("What ports do you need exposed to run this application? (comma-separated list): ")

    if ports.lower() == 'exit' or ports.lower() == 'quit':
        main_menu()

    return language, version, packageManager, os, dependencies, ports


def main_menu():
    print(ascii_art)
    print("Welcome to Dockerbot! A bot created in Python3 to help you automate some of those boring tasks")
    
    while True:
        print("\nPlease select an option:")
        print("1. Build Dockerfile")
        print("2. Generate Docker Compose")
        print("3. Inspect Dockerfile")
        print("4. Chat with Dockerbot")
        print("5. Exit Dockerbot")

        choice = input("> ")

        if choice in ["1", "build", "Build", "build dockerfile", "Build Dockerfile"]:
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
            file_path = input("Enter the path to the Dockerfile: ")
            with open(file_path, 'r') as f:
                dockerfile = f.read()
            results = analyze_dockerfile(dockerfile)
            print(f"\nHere's the description of your Dockerfile:\n{results}\n")

        elif choice == "4":
            print(ascii_art)
            prompt = input("Enter a prompt to generate a Dockerfile: ")
            dockerfile = generate_dockerfile_from_prompt(prompt)
            print(f"Here's your Dockerfile:\n{dockerfile}\n")
            filename = input("Enter a filename to save the Dockerfile: ")
            write_dockerfile(filename, dockerfile)
            print(f"\nYour Dockerfile has been saved to {filename}.\n")

        elif choice in ["5", "Exit", "exit", "Quit", "quit"]:
            print(ascii_art)
            print("Thank you for using Dockerbot. Goodbye!")
            sys.exit()  # Exit the entire program

        else:
            print("Invalid choice. Please try again.")

# Generate the Dockerfile based on user inputs

def generate_dockerfile(language, version, packageManager, os, dependencies, ports):
    base_commands = {
        "alpine": ["FROM {}:{}-{}".format(language, version, os)],
        "ubuntu": ["FROM {}:{}".format(language, version)]
    }

    if packageManager == "npm":
        install_commands = [
            "RUN npm install -g npm",
            "COPY package*.json ./app/",
            "RUN npm install",
        ]
    elif packageManager == "yarn":
        install_commands = [
            "RUN npm install -g yarn",
            "COPY package*.json ./app/",
            "RUN yarn install",
        ]
    elif packageManager == "pip":
        install_commands = [
            "COPY requirements.txt /app",
            "RUN pip install -r /app/requirements.txt",
        ]
    else:
        install_commands = []

    all_commands = []
    all_commands.extend(base_commands[os])
    all_commands.extend(install_commands)

    if dependencies:
        if packageManager in ["npm", "yarn"]:
            all_commands.append("COPY . .")
            all_commands.append("RUN {} install".format(packageManager))
        elif packageManager == "pip":
            all_commands.append("COPY . /app")
        else:
            pass

    if ports:
        port_list = ports.split(",")
        for port in port_list:
            all_commands.append("EXPOSE {}".format(port))

    dockerfile = "\n".join(all_commands)
    return dockerfile

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
