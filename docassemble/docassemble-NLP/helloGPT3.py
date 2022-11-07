import openai

openai.api_key = get_config('open ai api key')

def gpt3_completion(
    prompt, engine='text-davinci-002', 
    temp=0.7, 
    top_p=1.0, 
    tokens=400, 
    freq_pen=0.0, 
    pres_pen=0.0, 
    stop=['<<END>>']):
        prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
        response = openai.Completion.create(
                engine=engine,
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
        text = response['choices'][0]['text'].strip()
        return text

    if __name__ == '__main__':
        prompt = "Write the winning reasoning for a small claims demand letter in a personal injury case."
        response = gpt3_completion(prompt)
        print(response)