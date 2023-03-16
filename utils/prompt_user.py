from utils.bot_logo import generate_ascii_art
from utils.docker_images import knowledge_base
from validations.version_validation import validate_version
from validations.package_manager_validation import validate_package_manager

ascii_art = generate_ascii_art()
knowledge_base_file = "utils/docker_images.py"

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

def prompt_user():
    print(ascii_art)

    global knowledge_base

    if file_exists(knowledge_base_file):
        # if knowledge base file exists, import its contents
        from utils.docker_images import knowledge_base
    else:
        # otherwise, initialize an empty knowledge base
        knowledge_base = {}

    knowledge_base_list = list(knowledge_base.keys())

    language = ""    

    while True:
        language = input("What programming language, framework or distrobution do you want to use? (python, nodejs, ubuntu): ")

        if language.lower() == 'exit' or language.lower() == 'quit':
            from utils.bot_menu import main_menu
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
        from utils.bot_menu import main_menu
        main_menu()

    version = validate_version(version)

    packageManager = input("What package manager do you want to install application dependencies with? (npm, yarn, pip): ")

    if packageManager.lower() == 'exit' or packageManager.lower() == 'quit':
        from utils.bot_menu import main_menu
        main_menu()

    packageManager = validate_package_manager(packageManager)

    os = input("What operating system do you want to base your image on? (alpine, ubuntu): ")

    if os.lower() == 'exit' or os.lower() == 'quit':
        from utils.bot_menu import main_menu
        main_menu()

    dependencies_choice = input("Do you want to input dependencies manually or read from a file such as package.json? (m/f): ")

    if dependencies_choice.lower() == 'exit' or dependencies_choice.lower() == 'quit':
        from utils.bot_menu import main_menu
        main_menu()

    while dependencies_choice not in ["m", "f"]: # Add valid options for dependencies choice
         dependencies_choice = input("Invalid input. Please enter a valid option from the list (m/f): ")

    dependencies = [] 

    if dependencies_choice.lower() == "m":
        dependencies = input("What packages or dependencies do you need? (comma-separated list): ")
    elif dependencies_choice.lower() == "f":
        pass
     
    ports = input("What ports do you need exposed to run this application? (comma-separated list): ")

    while not all(port.strip().isdigit() for port in ports.split(',')):
        ports = input("What ports do you need exposed to run this application? (comma-separated list): ")
        print("Error: Port numbers must be numeric only.")

        if ports.lower() == 'exit' or ports.lower() == 'quit':
            from utils.bot_menu import main_menu
            main_menu()

    return language, version, packageManager, os, dependencies, ports
