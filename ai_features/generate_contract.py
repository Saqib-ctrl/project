import openai

openai.api_key = "your_openai_api_key"

def generate_contract(contract_data):
    prompt = f"Generate an employment contract using this information:\n{contract_data}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=400
    )
    return response.choices[0].text.strip()