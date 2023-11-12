# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
client = OpenAI(api_key="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")

response = client.completions.create(
  model="text-davinci-002",
  prompt="write a motivational quote for me",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].text)
