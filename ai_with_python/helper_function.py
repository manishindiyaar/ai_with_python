import os


import csv
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
# client = AzureOpenAI(
#   api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
#   api_version = "2024-08-01-preview",
#   azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
# )

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# def azure_openai(prompt):

#     response = client.chat.completions.create(
#     model="gpt-4", # model = "deployment_name".
#     messages=[
#         {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
#         {"role": "user", "content": prompt}
#     ]
# )
#     return response.choices[0].message.content

# print(azure_openai("What is the capital of Nigeria?"))
    






def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print("_"*100)
        print(response)
        print("_"*100)
        print("\n")
    except TypeError as e:
        print("Error:", str(e))


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response


def get_chat_completion(prompt, history):
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt_with_history},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

