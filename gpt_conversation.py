import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai = OpenAI()

gpt_model = "gpt-4o-mini"


gpt_system = "You are a counter that remembers the number given by user and return the sum. initialy the number is 0. when user gives next number you have to add that number with prevoius number"


gpt_messages = []
user_messages = []

def call_gpt(message):
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, user in zip(gpt_messages, user_messages):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": user})
    messages.append({"role": "user", "content": message}) 
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content 


# print(call_gpt("what are you")) 

while True:
    user = input("User: ")
    gpt = call_gpt(user)
    print(f"GPT: {gpt}")
    gpt_messages.append(gpt)
    user_messages.append(user) 