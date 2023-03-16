import re
import json

def analyze_dockerfile(dockerfile):

    # Regular expressions to extract relevant information from the Dockerfile
    base_image_regex = r'^FROM\s+(.*)$'
    package_regex = r'^(RUN|RUN\s+--\s+.*\s+)apt-get install -y (.*)$'
    exposed_port_regex = r'^EXPOSE\s+(.*)$'

    # Regular expressions to extract relevant information from the application files
    package_file_regex = r'(package\.json|requirements\.txt|Gemfile)'

    # Initialize variables to store information extracted from the Dockerfile
    base_image = None
    packages = []
    exposed_ports = []

    # Parse the Dockerfile for base image, packages, and exposed ports
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

    # Parse the Dockerfile for application files
    for line in dockerfile.split('\n'):
        package_file_match = re.search(package_file_regex, line)
        if package_file_match:
            package_file = package_file_match.group(1)
            with open(package_file, 'r') as f:
                file_content = f.read()
                if package_file == 'package.json':
                    dependencies = json.loads(file_content).get('dependencies', [])
                elif package_file == 'requirements.txt':
                    dependencies = file_content.strip().split('\n')
                elif package_file == 'Gemfile':
                    dependencies = re.findall(r'gem\s+([^\s]+)', file_content)
                packages.extend(dependencies)

    # Generate a description based on the extracted information
    description = f"This Dockerfile uses {base_image} as the base image \n\nInstalls the following packages: {', '.join(packages)}."
    if exposed_ports:
        description += f" \n\nIt also exposes the following ports: {', '.join(exposed_ports)}."

    return description

