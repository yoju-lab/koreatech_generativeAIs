# from : https://platform.openai.com/docs/quickstart?context=python
from openai import OpenAI
client = OpenAI()

def conn_chatgpt(input_text):
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # model="gpt-4",
    messages=[
      {"role": "user", "content": input_text}
    ],
    # temperature=2,
  )
  # completion
  # ChatCompletion(id='chatcmpl-8dtFFmhIlqnkwAcWUKs09cOpRTS7Z', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='1. 헬스케어 데이터 분석가를 위한 데이터 분석 기초 과정\n2. 헬스케어 데이터 분석가로 성장하기 위한 고급 데이터 분석 과정\n3. 헬스케어 분야에서 활용되는 빅데이터 분석과 데이터 시각화 과정\n4. 헬스케어 데이터 분석가를 위한 예측 분석과 머신 러닝 과정\n5. 헬스케어 데이터 분석과정에서의 통계적 분석 방법과 실험설계 과정', role='assistant', function_call=None, tool_calls=None))], created=1704517845, model='gpt-3.5-turbo-0613', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=188, prompt_tokens=60, total_tokens=248))
  output_text = completion.choices[0].message.content
  # print(output_text)
  return output_text
  pass

if __name__ == "__main__":
  input_text = "인공지능을 한 줄로 알려줘"
  input_text = "헬스케어 분야  데이터 분석가 과정 강의명을 한 문장으로 5가지 예시 작성, 문장 끝엔 과정 붙이기"
  output_text = conn_chatgpt(input_text)

  pass