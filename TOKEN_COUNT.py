# Write a function that prompts me a user to enter a prompt, then print the number of tokens the inputted prompt would generate
import tiktoken

def count_tokens(prompt):
    """
    Counts the number of tokens in a given prompt.
    
    Args:
        prompt (str): The prompt to count tokens for.
        
    Returns:
        int: The number of tokens in the prompt.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(prompt))
    return num_tokens

user_prompt = input("Enter a prompt: ")
token_count = count_tokens(user_prompt)
print(f"The prompt contains {token_count} tokens.") 