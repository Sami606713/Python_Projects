# make our views
from django.shortcuts import render,redirect
from django.http import HttpResponse
import json
import random
from .models import Conversation
# open AI part
import openai
def bot_response(text):
    openai.api_key = 'your_api_key'
    # client=OpenAI(api_key="my_api_key")
    response = openai.completions.create(
    model="gpt-4-vision-preview",
    prompt=text,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response
# Open AI end

def index(requests):
    messages=[]
    dic={
        "name":"""Decode stage decode the fetch instruction in this format so that the processor can understand. 
Processor understand only binary format"""

    }
    choice=["hi","hy","nice"]
    update_input=None
    if(requests.method=="POST"):
        user_input=requests.POST.get("user_input")
        if user_input in dic:
            response=dic[user_input]
            messages.append(response)
        else:
            response=random.choice(choice)
            messages.append(response)

        update_input=user_input
        conversation=Conversation(user_input=user_input,response=response)
        conversation.save()

        # try:
        #     response=bot_response(user_input)
        #     messages.append(response)
        # except Exception as e:
        #     response=random.choice(choice)
        #     messages.append(response)
 
    context={
        "messages":messages,
        "user_input":update_input
    }
    return render(requests,"index.html",context)










# from django.shortcuts import render

# def index(request):
#     messages = []
#     if request.method == 'POST':
#         user_input = request.POST.get('user_input')
#         messages.append(user_input)

#         if user_input.lower() == 'hi':
#             messages.append("How can I help you today?")

#     context = {
#         'messages': messages,
#     }
#     return render(request, 'index.html', context)
