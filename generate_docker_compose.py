import os
import re


def generate_docker_compose(dockerfile_path: str) -> str:
    """
    Generates Docker Compose YAML configuration from a Dockerfile path
    :param dockerfile_path: str, path to Dockerfile
    :return: str, Docker Compose YAML configuration
    """
    # Get the directory containing the Dockerfile
    dockerfile_dir = os.path.dirname(dockerfile_path)
    
    # Get the image name from the Dockerfile
    with open(dockerfile_path, "r") as dockerfile:
        dockerfile_contents = dockerfile.read()
    image_name_match = re.search(r"FROM\s+([\w-]+)", dockerfile_contents)
    if not image_name_match:
        raise ValueError("Unable to extract image name from Dockerfile")
    image_name = image_name_match.group(1)
    
    # Generate the Docker Compose YAML configuration
    yaml_config = f"version: '3'\n\nservices:\n  {image_name}:\n    build:\n      context: {dockerfile_dir}\n"
    
    return yaml_config

