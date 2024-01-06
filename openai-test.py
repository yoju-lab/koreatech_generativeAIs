# from : https://platform.openai.com/docs/quickstart?context=python
from openai import OpenAI
client = OpenAI()

input_text = "인공지능을 한 줄로 알려줘"
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": input_text}
  ]
)

print(completion.choices[0].message.content)
pass