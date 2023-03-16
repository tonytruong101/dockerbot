import openai

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
