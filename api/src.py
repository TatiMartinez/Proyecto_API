import os
import openai

openai.api_key ="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"




def userMessage(payload, conversationId):
    print(payload)
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    contexto = "Lo que sigue es una conversación con un asistente de IA. El asistente es servicial, creativo, inteligente y muy amable."

    # obtner la lista de registros guardados en la base de datos por converstaionId
    messages = [{"payload": "hola", "botResponse": "Muy  bien y vos"}, {"payload": "perfecto", "botResponse": "que lindo"}]
    conversation = "" 
    for message in messages:
        conversation += "\nHuman: " + message["payload"]
        conversation += "\nAI: "+ message["botResponse"]
    
    conversation += " \nHuman: "+ payload + "\n AI:" 


    response = openai.Completion.create(
        model="text-davinci-002",
        # prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
        prompt= contexto + conversation,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    #print("response", response["choices"][0] ["text"] )
    bot = response["choices"][0] ["text"]
    return bot
