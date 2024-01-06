# from : https://platform.openai.com/docs/quickstart?context=python
from openai import OpenAI
client = OpenAI()

input_text = "인공지능을 한 줄로 알려줘"
input_text = "헬스케어 분야  데이터 분석가 과정 강의명을 한 문장으로 5가지 예시 작성, 문장 끝엔 과정 붙이기"
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  # model="gpt-4",
  messages=[
    {"role": "user", "content": input_text}
  ],
  # temperature=2,
)

print(completion.choices[0].message.content)
pass