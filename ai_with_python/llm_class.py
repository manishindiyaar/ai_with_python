import os
from openai import AzureOpenAI
from dotenv import load_dotenv


load_dotenv()

class LLM:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-08-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

    def get_response(self, prompt):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system", "content": "You are Helpfull assistant"
                    },
                    {
                        "role": "user", "content": prompt
                    }
                ],
                temperature=0.0


            )   
            return completion.choices[0].message.content
        except Exception as e:
            error_message = f"failed to fetch response from AzureOpenAI : {str(e)}"
            print(error_message)
            return error_message

    def print_response(self, prompt):

        response = self.get_response(prompt)
        if response:
            print("_"*100)
            print(response)
            print("_"*100)
            print("\n")


if __name__ == "__main__":
    ai_assistant = LLM()
    response = ai_assistant.get_response("What is the capital of Nigeria?")
    print(response)                   