import openai

openai.api_key = "your_openai_api_key"

def generate_job_posting(job_data):
    prompt = f"You are an HR assistant. Create a job posting using the following details:\n{job_data}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()