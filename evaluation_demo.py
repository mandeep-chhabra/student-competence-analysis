# Minimal demo: Run StarCoder on a toy student Python snippet
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model & tokenizer
model_name = "bigcode/starcoderbase"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

# Example: buggy student code
student_code = """
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
"""

# Prompt the model for analysis
prompt = f"Analyze the following student Python code and generate 2 reflective questions to test conceptual understanding without giving the solution:\n\n{student_code}\n\nAnalysis and Prompts:"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_length=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

