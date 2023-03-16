from utils.prompt_user import prompt_user
from utils.bot_logo import generate_ascii_art
from utils.bot_gpt_prompt import generate_dockerfile_from_prompt 
from utils.docker_images import knowledge_base
from utils.dockerfile_generator import generate_dockerfile
from utils.generate_dockercompose import generate_docker_compose
from utils.analyze_dockerfile import analyze_dockerfile


import openai
import sys

ascii_art = generate_ascii_art()

knowledge_base_file = "utils/docker_images.py"

openai.api_key = ''

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
            return main_menu

# Write dockerfile
def write_dockerfile(filename, dockerfile):
    with open(filename, "w") as f:
        f.write(dockerfile)

# Close the app
def close_app():
    print("Goodbye!")
    sys.exit()

