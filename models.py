import openai


class Conversation:
    def __init__(self, prompt, num_of_round):
        self.prompt = prompt
        self.num_of_round = num_of_round
        self.messages = []
        self.messages.append({'role': 'system', 'content': prompt})

    def ask(self, question: str) -> str:
        try:
            self.messages.append({'role': 'user', 'content': question})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                temperature=0.5,
                max_tokens=2048,
                top_p=1,
            )
        except Exception as e:
            print(e)
            return e.__doc__
        message = response["choices"][0]["message"]["content"]
        # num_of_tokens = response['usage']['total_tokens']
        self.messages.append({"role": "assistant", "content": message})

        if len(self.messages) > self.num_of_round * 2 + 1:
            del self.messages[1:3]
        return message


if __name__ == '__main__':
    myPrompt = """你是一个中国厨师，用中文回答做菜的问题。你的回答需要满足以下要求:1. 你的回答必须是中文2. 回答限制在100个字以内"""
    conv = Conversation(myPrompt, 10)
    answer = conv.ask('你好')
    print(answer)
