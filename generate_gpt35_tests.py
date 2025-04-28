import openai
import pandas as pd
import os
import time

# Load your API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create the output directory if it doesn't exist
output_dir = "outputsGPT/gpt3.5"
os.makedirs(output_dir, exist_ok=True)

# Read the dataset
csv_path = "humaneval_prompts_with_difficulty.csv"
df = pd.read_csv(csv_path)

# Authors block to insert at the top of each file
authors_block = """\
# @Authors
# * Student Name: Mustafa Yavuz Engin
# * Student ID: 150200708

# * Student Name: Çiğdem Onur
# * Student ID: 150190022

"""

# Function to call OpenAI for code generation
def call_openai_code(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print("Error:", e)
        return ""

# Generate code and test files
for task_id in range(len(df)):
    print(f"[+] Processing Task {task_id}")

    problem_prompt = df.iloc[task_id]['prompt']

    # Request code
    code_prompt = f"Write a Python function that solves the following problem:\n{problem_prompt}"
    code_response = call_openai_code(code_prompt)
    with open(os.path.join(output_dir, f"task_{task_id}_code.py"), "w", encoding="utf-8") as f:
        f.write(authors_block + "\n\n" + code_response)

    # Request tests
    test_prompt = f"Write 3-5 Python unittest test cases for the following function:\n{problem_prompt}"
    test_response = call_openai_code(test_prompt)
    with open(os.path.join(output_dir, f"task_{task_id}_test.py"), "w", encoding="utf-8") as f:
        f.write(authors_block + "\n\n" + test_response)

    # Wait between API calls to avoid rate limits
    time.sleep(40)

print("\n[✔] All code and test files have been generated successfully.")
