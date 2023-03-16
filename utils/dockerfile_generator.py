from utils.bot_menu import prompt_user 

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
    elif packageManager == "bundler":
        install_commands = [
            "COPY Gemfile /app/Gemfile",
            "RUN gem install bundler",
	    "RUN bundle install",
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

    print("Generated Dockerfile:\n")
    print(dockerfile)

    while True:
        user_input = input("Are you satisfied with the generated Dockerfile? (y/n): ")
        if user_input.lower() == "y":
            break
        elif user_input.lower() == "n":
            print("Restarting...")
            return main_menu()

        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    return dockerfile
