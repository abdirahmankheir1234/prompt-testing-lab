# List of prompts used to test AI coding ability

prompts = [
    "Write a Python function to check if a number is prime.",
    "Write a Python function to reverse a string.",
    "Write a Python function that finds the largest number in a list.",
    "Write a Python function that counts vowels in a string."
]

def show_prompts():
    print("AI Prompt Testing Lab")
    print("---------------------")

    for i, prompt in enumerate(prompts, start=1):
        print(f"{i}. {prompt}")


if __name__ == "__main__":
    show_prompts()
    