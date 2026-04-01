import google.generativeai as genai
import os


def talk(question):
    #question=str(input())

    genai.configure(api_key="") #put your api key here

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(question)
    return response.text