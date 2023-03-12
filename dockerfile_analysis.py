import re

def analyze_dockerfile(dockerfile):


    # Regular expressions to extract relevant information from the Dockerfile
    base_image_regex = r'^FROM\s+(.*)$'
    package_regex = r'^(RUN|RUN\s+--\s+.*\s+)apt-get install -y (.*)$'
    exposed_port_regex = r'^EXPOSE\s+(.*)$'

    # Initialize variables to store information extracted from the Dockerfile
    base_image = None
    packages = []
    exposed_ports = []

    # Parse the Dockerfile
    for line in dockerfile.split('\n'):
        base_image_match = re.match(base_image_regex, line)
        package_match = re.match(package_regex, line)
        exposed_port_match = re.match(exposed_port_regex, line)

        if base_image_match:
            base_image = base_image_match.group(1)
        elif package_match:
            packages.extend(package_match.group(2).split())
        elif exposed_port_match:
            exposed_ports.extend(exposed_port_match.group(1).split())

    # Generate a description based on the extracted information
    description = f"This Dockerfile uses {base_image} as the base image and installs the following packages: {', '.join(packages)}."
    if exposed_ports:
        description += f" It also exposes the following ports: {', '.join(exposed_ports)}."

    return description

