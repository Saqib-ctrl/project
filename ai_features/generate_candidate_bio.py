import openai

openai.api_key = "your_openai_api_key"

def generate_candidate_bio(candidate_data):
    prompt = f"You are an HR expert. Write a short bio for the following candidate:\n{candidate_data}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()