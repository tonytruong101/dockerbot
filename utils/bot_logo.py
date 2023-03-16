import pyfiglet

def generate_ascii_art():
    text = "DOCKERBOT"
    ascii_art = pyfiglet.figlet_format(text)
    return ascii_art
