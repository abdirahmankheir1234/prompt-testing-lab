def evaluate_answer(prompt, answer, evaluation):
    print("Prompt:")
    print(prompt)

    print("\nAI Answer:")
    print(answer)

    print("\nEvaluation:")
    print(evaluation)


# Example test
if __name__ == "__main__":

    prompt = "Write a Python function to reverse a string."

    answer = """
def reverse_string(s):
    return s[::-1]
"""

    evaluation = """
This solution is correct because it uses Python slicing to reverse the string efficiently.
"""

    evaluate_answer(prompt, answer, evaluation)